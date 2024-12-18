function day6() {

    const input = require('fs').readFileSync('./day6.txt', 'utf-8');
    const matrix = input.split('\n').map(row => row.split(''));

    const guard = walk(copy(matrix));
    console.log('[D6P1]', guard.virginSteps);

    const loops = findLoops(matrix, guard.plan);
    console.log('[D6P2]', loops.infiniteLoopsFound);
}

const copy = (matrix) => (matrix.map(row => row.map(char => char)));
const directions = {
    up: {x: -1, y: 0, turn: 'right', symbol: '^'},
    right: {x: 0, y: 1, turn: 'down', symbol: '>'},
    down: {x: 1, y: 0, turn: 'left', symbol: 'v'},
    left: {x: 0, y: -1, turn: 'up', symbol: '<'},
}

function findLoops(matrix, floorPlan) {

    let infiniteLoopsFound = 0, loopCount = 0;

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {

            // only place items where the guard is suspected to have walked and not directly in front of him
            if (matrix[i][j] !== '#' && matrix[i][j] !== '^' && floorPlan[i][j] !== '.') {

                const newMatrix = copy(matrix);
                newMatrix[i][j] = '#';
                const caret = walk(newMatrix);

                if (caret.exitReason === 'infinite loop') infiniteLoopsFound++;
                loopCount++;
            }
        }
    }
    return {infiniteLoopsFound, loopCount};
}

function walk(matrix) {

    const caret = {
        x: matrix.findIndex(r => r.includes('^')),
        y: matrix[matrix.findIndex(r => r.includes('^'))].findIndex(char => char === '^'),
        steps: 1,
        virginSteps: 1,
        currentDirection: 'up',
        exitReason: 'end',
        plan: matrix,
    };

    const turnLog = new Set();
    while (true) {

        const x = caret.x + directions[caret.currentDirection].x;
        const y = caret.y + directions[caret.currentDirection].y;

        // we are out of the matrix
        if (!matrix[x] || !matrix[x][y]) break;

        // while in the matrix
        // we hit an obstacle: turn and check for infinite loop
        if (matrix[x] && matrix[x][y] === '#') {

            caret.currentDirection = directions[caret.currentDirection].turn;

            if (turnLog.has(`${caret.currentDirection} ${caret.x} ${caret.y}`)) {
                caret.exitReason = 'infinite loop';
                break;
            }

            turnLog.add(`${caret.currentDirection} ${caret.x} ${caret.y}`);
            continue;
        }

        // otherwise move caret
        matrix[caret.x][caret.y] = `${directions[caret.currentDirection].symbol}`;
        caret.y = y;
        caret.x = x;
        caret.steps++;

        if (matrix[x][y] === '.') caret.virginSteps++;
        matrix[x][y] = '0';
    }
    return caret;
}
day6();
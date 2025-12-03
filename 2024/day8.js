function day8() {

    const input = require('fs').readFileSync('./day8.txt', 'utf-8');
    const matrix = input.split('\n')
        .filter(row => row.length > 0)
        .map(row => row.split(''));

    const antennas = new Map(), antiNodes = new Set(), antiNodesResonance = new Set();

    const withinMatrix = ([x,y]) => (matrix[x] && matrix[x][y]);

    const registerAntiNode = (node, nextNodeDistance, level) => {

        if (!withinMatrix(node)) return;

        let [x, y] = node, [dx, dy] = nextNodeDistance;
        if (level === 1)  antiNodes.add(`${x},${y}`);
        antiNodesResonance.add(`${x},${y}`);
        registerAntiNode([x + dx, y + dy], nextNodeDistance, ++level);
    }

    const registerAntiNodesResonance = (current, next) => {

        let [cx, cy] = current, [nx, ny] = next;
        const [dx, dy] = [nx - cx, ny - cy];

        registerAntiNode([cx, cy], [-dx, -dy], 0);
        registerAntiNode([nx, ny], [dx, dy], 0);
    }

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] !== '.') (antennas[matrix[i][j]] ??= []).push([i, j]);
        }
    }

    Object.keys(antennas).filter(key => antennas[key]?.length > 1)
        .forEach(key => {

            for (let i = 0; i < antennas[key].length - 1; i++) {
                for (let j = i + 1; j < antennas[key].length; j++) {
                    registerAntiNodesResonance(antennas[key][i], antennas[key][j]);
                }
            }
        });

    console.log('[D8P1]', antiNodes.size);
    console.log('[D8P2]', antiNodesResonance.size);
}
day8();
function day9() {

    const input = require('fs').readFileSync('./day9.txt', 'utf-8');

    const numbers = input.split('').map(Number);
    const index = [];

    for (let i = 0; i < numbers.length; i++) {

        const fragments = i % 2 === 1 ?
            '.'.repeat(numbers[i]).split('') :
            (' '+ (i/2)).repeat(numbers[i]).trim().split(' ').map(Number);
        index.push(...fragments);
    }

    const pt1 = part1Defrag(index);
    const pt2 = part2Defrag(index);

    console.log('[D9P1]', checksum(pt1));
    console.log('[D9P2]', checksum(pt2));
}

function checksum(index) {

    let checksum = 0;

    for (let i = 0; i < index.length; i++) {
        if (index[i] === '.') continue;
        checksum += index[i] * i;
    }
    return checksum;
}

function part1Defrag(drive) {

    const index = [...drive];

    let noSwitch = false; // break the loop if no switch is made
    for (let i = 0 ; i < index.length; i++) {
        if (noSwitch) break;
        if (index[i] !== '.') continue;

        for (let j = index.length -1; j > i; j--) {

            if (index[j] === '.') {
                noSwitch = true;
                continue;
            }

            index[i] = index[j];
            index[j] = '.';
            noSwitch = false;
            break;
        }
    }
    return index;
}
function part2Defrag(drive) {

    const index = [...drive];
    const fileMap = {};

    index.forEach((value) => {
        if (value !== '.') {
            fileMap[value] ??= 0;
            fileMap[value]++;
        }
    });

    for (let i = index.length - 1; i > 0; i--) {
        if (index[i] !== '.') {
            const fileLength = fileMap[index[i]];
            for (let j = 0; j < i; j++) {
                if (index[j] === '.' && index.slice(j, j+fileLength).every(v => v === '.')) {
                    index.fill(index[i], j, j+fileLength);
                    index.fill('.', i-fileLength+1, i+1);
                    break;
                }
            }
        }
    }
    return index;
}
day9();
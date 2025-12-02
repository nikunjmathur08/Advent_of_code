function day5() {

    const input = require('fs').readFileSync('./day5.txt', 'utf8');
    const rows = input.split('\n');

    const controlMap = {};

    rows.filter(row => row.includes('|'))
        .map(row => row.split('|').map(Number))
        .forEach(([key, value]) => (controlMap[key] ??= []).push(value));

    const instructions = rows
        .filter(row => row.includes(','))
        .map(row => row.split(',').map(Number));

    const sortByInstructions = (a, b) => {
        if (controlMap[a]?.includes(b)) return -1;
        if (controlMap[b]?.includes(a)) return 1;
        return 0;
    }
    const isValid = (instructions) => {
        return [...instructions].sort(sortByInstructions).join(',') === instructions.join(',');
    }

    let validCount = 0, repairCount = 0;

    instructions.forEach(instruction => {
           isValid(instruction) ?
               validCount  += instruction[Math.floor(instruction.length / 2)] :
               repairCount += instruction.sort(sortByInstructions)[Math.floor(instruction.length / 2)];
        }
    )

    console.log('[D5P1]', validCount);
    console.log('[D5P2]', repairCount);
}

day5();
function day7() {

    const input = require('fs').readFileSync('./day7.txt', 'utf-8');
    const equations = input
        .split('\n')
        .filter(row => row.length > 0)
        .map(row => row.split(': '))
        .map(([key, values]) => [Number(key), values.split(' ').map(Number)]);

    const calculate = (numbers, operator, current, target, supportConcat) => {

        if (target === current && numbers.length === 0) return true;
        if (current > target) return false;
        if (numbers.length === 0) return false;

        switch (operator) {
            case '*':
                current *= numbers[0];
                break;
            case '+':
                current += numbers[0];
                break;
            case '|':
                current = Number(`${current}${numbers[0]}`);
                break;
            default: return false;
        }

        return  calculate(numbers.slice(1), '*', current, target, supportConcat) ||
                calculate(numbers.slice(1), '+', current, target, supportConcat) ||
                (supportConcat && calculate(numbers.slice(1), '|', current, target, supportConcat));
    }

    const isPossible = ([result, nums]) => calculate(nums, '+', 0, result, false);
    const isPossibleWithConcat = ([result, nums]) => calculate(nums, '+', 0, result, true);

    const sum = equations
        .filter(isPossible)
        .map(equation => equation[0])
        .reduce((acc, curr) => acc + curr, 0);

    const sumWithOr = equations
        .filter(isPossibleWithConcat)
        .map(equation => equation[0])
        .reduce((acc, curr) => acc + curr, 0);

    console.log('[P7D1]', sum);
    console.log('[P7D2]', sumWithOr);
}

day7();
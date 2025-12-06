import sys
from functools import reduce
import operator
def cephalopod_part1(lines):
    rows = len(lines)
    cols = max(len(l) for l in lines)
    lines = [l.ljust(cols) for l in lines]

    sep = [all(lines[r][c] == " " for r in range(rows)) for c in range(cols)]

    groups = []
    in_group = False
    for c in range(cols):
        if not sep[c] and not in_group:
            start = c
            in_group = True
        elif sep[c] and in_group:
            groups.append((start, c - 1))
            in_group = False
    if in_group:
        groups.append((start, cols - 1))

    total = 0

    for start, end in groups:
        tokens = []
        for r in range(rows):
            t = lines[r][start:end+1].strip()
            if t:
                tokens.append(t)

        op = tokens[-1]
        nums = [int(t) for t in tokens[:-1]]

        if op == "+":
            val = sum(nums)
        else:
            val = reduce(operator.mul, nums, 1)

        total += val

    return total

def cephalopod_part2(lines):
    rows = len(lines)
    cols = max(len(l) for l in lines)
    lines = [l.ljust(cols) for l in lines]

    bottom = lines[-1]

    sep = [all(lines[r][c] == " " for r in range(rows)) for c in range(cols)]

    groups = []
    in_group = False
    for c in range(cols):
        if not sep[c] and not in_group:
            start = c
            in_group = True
        elif sep[c] and in_group:
            groups.append((start, c - 1))
            in_group = False
    if in_group:
        groups.append((start, cols - 1))

    total = 0

    for start, end in groups:
        op = None
        for c in range(start, end + 1):
            if bottom[c] in "+*":
                op = bottom[c]
                break
        if op is None:
            continue

        numbers = []
        for c in range(end, start - 1, -1):
            digits = []
            for r in range(rows - 1):
                ch = lines[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                numbers.append(int("".join(digits)))

        if op == "+":
            val = sum(numbers)
        else:
            val = reduce(operator.mul, numbers, 1)

        total += val

    return total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python day6.py <input-file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        lines = [line.rstrip("\n") for line in f]

    part1 = cephalopod_part1(lines)
    part2 = cephalopod_part2(lines)

    print("Part 1 (row-wise interpretation):", part1)
    print("Part 2 (true cephalopod column-wise interpretation):", part2)

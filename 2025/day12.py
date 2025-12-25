import sys
from typing import Dict, List, Tuple


sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "2025/day12.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def parse_lines(
    lines: List[str],
) -> Tuple[Dict[int, List[List[str]]], List[Tuple[Tuple[int, int], List[int]]]]:
    shapes = {}
    last_shape = None

    regions = []

    for line in lines:
        if line == "":
            continue
        elif "#" in line or "." in line:
            shapes[last_shape].append(list(line))
        else:
            split = line.split(":")
            if split[-1] == "":
                last_shape = int(split[0])
                shapes[last_shape] = []
            else:
                area = tuple([int(x) for x in split[0].split("x")])
                regions.append((area, [int(x) for x in split[-1].strip().split()]))

    return (shapes, regions)


def part_one():
    lines = read_lines_to_list()
    answer = 0

    _shapes, regions = parse_lines(lines)

    for size, presents in regions:
        width = size[0]
        height = size[1]

        total_area = width * height

        if 9 * sum(presents) <= total_area:
            answer += 1

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    print(f"Part 2: {answer}")


part_one()
part_two()

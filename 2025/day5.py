def parse_input(filepath):
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    ids = [int(x) for x in id_lines if x]

    return ranges, ids


def part1_count_fresh(ranges, ids):
    """Count how many IDs from the second section fall into ANY fresh range."""
    fresh_count = 0
    for ingredient_id in ids:
        if any(start <= ingredient_id <= end for start, end in ranges):
            fresh_count += 1
    return fresh_count


def merge_ranges(ranges):
    """Merge overlapping or adjacent ranges for Part 2."""
    if not ranges:
        return []

    # Sort by start
    ranges.sort()

    merged = [ranges[0]]

    for curr_start, curr_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if curr_start <= last_end + 1:  
            # Overlaps or touches → extend the range
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append((curr_start, curr_end))

    return merged


def part2_total_fresh_ids(ranges):
    """Compute total number of unique ingredient IDs considered fresh."""
    merged = merge_ranges(ranges)

    total = 0
    for start, end in merged:
        total += (end - start + 1)

    return total


if __name__ == "__main__":
    path = "2025/day5.txt"

    ranges, ids = parse_input(path)

    p1 = part1_count_fresh(ranges, ids)
    print("Part 1 - Fresh ingredient IDs among the available ones:", p1)

    p2 = part2_total_fresh_ids(ranges)
    print("Part 2 - Total ingredient IDs considered fresh:", p2)
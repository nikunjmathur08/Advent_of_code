def solve(filename: str):
    with open(filename, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    start_row = start_col = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    if start_row is None:
        raise ValueError("No starting point 'S' found")

    # PART 1: Classical beams (deduplicated)
    active_beams = {start_col}
    split_count = 0

    for r in range(start_row + 1, rows):
        next_beams = set()

        for c in active_beams:
            if not (0 <= c < cols):
                continue

            cell = grid[r][c]

            if cell == '.':
                next_beams.add(c)
            elif cell == '^':
                split_count += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)

        active_beams = next_beams
        if not active_beams:
            break

    # PART 2: Quantum timelines (no merging)
    timelines = {start_col: 1}

    for r in range(start_row + 1, rows):
        next_timelines = {}

        for c, count in timelines.items():
            if not (0 <= c < cols):
                continue

            cell = grid[r][c]

            if cell == '.':
                next_timelines[c] = next_timelines.get(c, 0) + count

            elif cell == '^':
                left = c - 1
                right = c + 1
                if 0 <= left < cols:
                    next_timelines[left] = next_timelines.get(left, 0) + count
                if 0 <= right < cols:
                    next_timelines[right] = next_timelines.get(right, 0) + count

        timelines = next_timelines
        if not timelines:
            break

    total_timelines = sum(timelines.values())

    return split_count, total_timelines


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python day7.py <input_file>")
        sys.exit(1)

    part1, part2 = solve(sys.argv[1])
    print("Part 1 (splits):", part1)
    print("Part 2 (timelines):", part2)
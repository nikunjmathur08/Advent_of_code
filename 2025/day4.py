def count_accessible_immediate(grid):
    """Part 1: Count rolls that initially have <4 adjacent @ neighbors."""
    rows = len(grid)
    cols = len(grid[0])

    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),         ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            cnt = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        cnt += 1

            if cnt < 4:
                accessible += 1

    return accessible


def total_removable(grid):
    """Part 2: Iteratively remove newly accessible rolls until none remain."""
    rows = len(grid)
    cols = len(grid[0])

    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),         ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    g = [list(row) for row in grid]
    removed_total = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if g[r][c] != '@':
                    continue

                cnt = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if g[nr][nc] == '@':
                            cnt += 1

                if cnt < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            g[r][c] = '.'

        removed_total += len(to_remove)

    return removed_total


def main():
    INPUT_PATH = "2025/day4.txt"

    with open(INPUT_PATH, "r") as f:
        grid = [line.rstrip("\n") for line in f]

    part1 = count_accessible_immediate(grid)
    print("Part 1: Initially accessible rolls =", part1)

    part2 = total_removable(grid)
    print("Part 2: Total removable rolls =", part2)


if __name__ == "__main__":
    main()

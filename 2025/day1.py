def compute_passwords(path_to_input):
    pos = 50
    part1 = 0
    part2 = 0

    with open(path_to_input, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            step = 1 if direction == "R" else -1

            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    part2 += 1

            if pos == 0:
                part1 += 1

    return part1, part2

p1, p2 = compute_passwords("2025/day1.txt")
print("Part 1:", p1)
print("Part 2:", p2)

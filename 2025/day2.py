def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def sum_invalid_ids(path_to_input):
    with open(path_to_input, "r") as f:
        line = f.read().strip()

    total = 0

    for part in line.split(","):
        if not part:
            continue

        lo_str, hi_str = part.split("-")
        lo = int(lo_str)
        hi = int(hi_str)

        for n in range(lo, hi + 1):
            if is_invalid_id(n):
                total += n

    return total

def is_invalid_id_part2(n: int) -> bool:
    s = str(n)
    length = len(s)

    for k in range(2, length + 1):
        if length % k != 0:
            continue

        segment_len = length // k
        segment = s[:segment_len]

        if segment * k == s:
            return True

    return False


def sum_invalid_ids_part2(path_to_input):
    with open(path_to_input, "r") as f:
        line = f.read().strip()

    total = 0

    for part in line.split(","):
        if not part:
            continue

        lo_str, hi_str = part.split("-")
        lo = int(lo_str)
        hi = int(hi_str)

        for n in range(lo, hi + 1):
            if is_invalid_id_part2(n):
                total += n

    return total

print("Part 1:", sum_invalid_ids("2025/day2.txt"))
print("Part 2:", sum_invalid_ids_part2("2025/day2.txt"))
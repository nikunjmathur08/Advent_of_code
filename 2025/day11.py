INPUT_FILE = "day11.txt"

graph = {}
with open(INPUT_FILE, "r") as f:
    for devices in [line.strip().split() for line in f]:
        graph[devices[0][:-1]] = devices[1:]

def traverse(device, end, visited, scores):
    if device == end:
        return 1
    if device in visited or device == "out":
        return 0
    if device in scores:
        return scores[device]
    visited.add(device)
    total = sum([traverse(output, end, visited, scores) for output in graph[device]])
    visited.remove(device)
    scores[device] = total
    return total

# Part1
print(traverse("you", "out", set(), {}))

# Part2
a1 = traverse("svr", "fft", set(), {})
a2 = traverse("fft", "dac", set(), {})
a3 = traverse("dac", "out", set(), {})
b1 = traverse("svr", "dac", set(), {})
b2 = traverse("dac", "fft", set(), {})
b3 = traverse("fft", "out", set(), {})
print(a1*a2*a3 + b1*b2*b3)

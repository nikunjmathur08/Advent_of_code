from collections import defaultdict
from functools import cache

# Parse and build graph
def parse_input(file_path):
    """
    Reads the input file and returns a list of connections.
    """
    with open(file_path, 'r') as f:
        connections = [line.strip().split('-') for line in f.readlines()]
    return connections

def build_graph(connections):
    """
    Builds an adjacency list representation of the graph from the connections.
    """
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

# Triangle detection
def find_triangles(graph):
    """
    Finds all triangles (sets of three fully-connected nodes) in the graph.
    """
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors & graph[neighbor]
            for cn in common_neighbors:
                triangle = tuple(sorted([node, neighbor, cn]))
                triangles.add(triangle)
    return triangles

def count_triangles_with_t(triangles):
    """
    Counts the triangles where at least one node starts with 't'.
    """
    return sum(1 for triangle in triangles if any(node.startswith('t') for node in triangle))

# Clique detection
def find_largest_clique(graph):
    """
    Finds the largest clique (set of fully-connected nodes) in the graph.
    """
    def is_clique(nodes):
        return all(graph[a].issuperset(nodes - {a}) for a in nodes)

    largest_clique = set()
    nodes = list(graph.keys())

    def backtrack(current_clique, remaining_nodes):
        nonlocal largest_clique
        if len(current_clique) > len(largest_clique):
            largest_clique = set(current_clique)

        for i, node in enumerate(remaining_nodes):
            new_clique = current_clique | {node}
            if is_clique(new_clique):
                backtrack(new_clique, remaining_nodes[i+1:])

    backtrack(set(), nodes)  # Use a list for remaining_nodes
    return largest_clique

def get_password(largest_clique):
    """
    Generates the password for the LAN party from the largest clique.
    """
    return ",".join(sorted(largest_clique))

# Pathfinding and shortest path calculation
posi = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

arr_pads = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

def get_pos(arr, code):
    for i, row in enumerate(arr):
        if code in row:
            return (i, row.index(code))

@cache
def shortest(start, end, layers):
    if start == "<" and end == ">":
        pass
    if isinstance(start, str):
        start = get_pos(arr_pads, start)
    if isinstance(end, str):
        end = get_pos(arr_pads, end)

    if layers == 0:
        return 1
    vert, hori = None, None
    if end[0] < start[0]:
        vert = "^"
    elif end[0] > start[0]:
        vert = "v"
    if end[1] < start[1]:
        hori = "<"
    elif end[1] > start[1]:
        hori = ">"

    if not hori and not vert:
        return shortest("A", "A", layers - 1)
    elif not hori:
        return shortest("A", vert, layers - 1) + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1) + shortest(vert, "A", layers - 1)
    elif not vert:
        return shortest("A", hori, layers - 1) + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1) + shortest(hori, "A", layers - 1)
    else:
        return min(
            shortest("A", hori, layers - 1) +
            (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1) +
            shortest(hori, vert, layers - 1) +
            (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1) +
            shortest(vert, "A", layers - 1),
            shortest("A", vert, layers - 1) +
            (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1) +
            shortest(vert, hori, layers - 1) +
            (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1) +
            shortest(hori, "A", layers - 1)
        )

def main():
    input_file = "day21.txt"  # Change this to your input file's name
    connections = parse_input(input_file)
    graph = build_graph(connections)

    # Part 1: Find triangles with at least one node starting with 't'
    triangles = find_triangles(graph)
    triangles_with_t_count = count_triangles_with_t(triangles)
    print(f"Total triangles with at least one 't' computer: {triangles_with_t_count}")

    # Part 2: Find the largest clique and get the LAN party password
    largest_clique = find_largest_clique(graph)
    password = get_password(largest_clique)
    print(f"Password to get into the LAN party: {password}")

    # Part 3: Shortest path calculations
    score = 0
    while True:
        inputval = input("Enter input (or press Enter to finish): ")
        if not inputval:
            break
        intval = int(inputval[:3])
        total = 0
        for startp, endp in zip("A" + inputval[:3], inputval):
            total += shortest(get_pos(posi, startp), get_pos(posi, endp), 3)
        print(f"{intval} -> Total: {total}")
        score += intval * total
    print(f"Final score: {score}")

if __name__ == "__main__":
    main()

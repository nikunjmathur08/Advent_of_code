def is_order_correct(order, rules):
    """Check if a given order satisfies the rules."""
    index_map = {page: i for i, page in enumerate(order)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def order_pages(order, rules):
    """Reorder pages based on rules."""
    from collections import defaultdict, deque

    # Build graph and in-degree count for topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x]  # Ensure every node appears in in_degree

    # Filter graph to include only nodes in the current update
    nodes = set(order)
    graph = {k: [v for v in vs if v in nodes] for k, vs in graph.items() if k in nodes}
    in_degree = {k: in_degree[k] for k in nodes}

    # Detect cycles using Kahn's algorithm
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []
    visited_count = 0

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        visited_count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if a cycle exists
    if visited_count != len(nodes):
        print(f"Cycle detected in update: {order}")
        print(f"Nodes involved in cycle: {set(nodes) - set(sorted_order)}")
        return []

    return sorted_order

def parse_input(file_path):
    """Parse input file into rules and updates."""
    with open(file_path, 'r') as file:
        content = file.read().strip()

    rules_section, updates_section = content.split('\n\n')

    # Parse rules
    rules = []
    for line in rules_section.split('\n'):
        x, y = map(int, line.split('|'))
        rules.append((x, y))

    # Parse updates
    updates = []
    for line in updates_section.split('\n'):
        updates.append(list(map(int, line.split(','))))

    return rules, updates

def main():
    # Read input from file
    input_file = 'day5.txt'
    rules, updates = parse_input(input_file)

    incorrect_middle_sum = 0
    for update in updates:
        if not is_order_correct(update, rules):
            ordered_update = order_pages(update, rules)
            if not ordered_update:
                print(f"Warning: Could not reorder update {update} due to cyclic dependencies.")
                continue  # Skip this update

            middle_page = ordered_update[len(ordered_update) // 2]
            incorrect_middle_sum += middle_page

    print("Sum of middle pages of incorrectly-ordered updates:", incorrect_middle_sum)

if __name__ == "__main__":
    main()

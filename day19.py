def count_ways_to_construct(design, patterns, memo=None):
    if memo is None:
        memo = {}
    if design in memo:  # Check memoization to avoid redundant calculations
        return memo[design]
    if not design:  # If the design is empty, there's exactly one way to construct it (do nothing)
        return 1

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):  # If the design starts with this pattern
            # Count ways to construct the remaining part of the design
            total_ways += count_ways_to_construct(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways  # Store the result in memo
    return total_ways


def total_arrangement_ways(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_construct(design, patterns)
    return total_ways


def read_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # First line contains the towel patterns (comma-separated)
    patterns = [pattern.strip() for pattern in lines[0].split(",")]
    
    # Remaining lines are the desired designs
    designs = lines[2:]  # Skip the blank line after patterns
    return patterns, designs


# Main execution
if __name__ == "__main__":
    input_file = "day19.txt"  # Replace with your input file name
    patterns_list, designs_list = read_input_from_file(input_file)
    total_ways = total_arrangement_ways(patterns_list, designs_list)
    print(f"Total number of ways to arrange towels: {total_ways}")

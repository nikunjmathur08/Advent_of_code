def calculate_list_distance(input_str):
    # Split the input string into lines
    lines = input_str.strip().split('\n')
    
    # Separate left and right lists
    left_list = []
    right_list = []
    
    # Parse each line
    for line in lines:
        # Split the line into left and right numbers, handling multiple whitespace
        parts = line.split()
        if len(parts) == 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate distances between paired numbers
    distances = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]
    
    # Calculate and return the total distance
    total_distance = sum(distances)
    
    return total_distance

# Read input from the document
with open('day1.txt', 'r') as file:
    input_str = file.read()

# Calculate and print the total distance
total_distance = calculate_list_distance(input_str)
print(f"Total Distance: {total_distance}")
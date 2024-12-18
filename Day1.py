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

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of numbers in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        # Multiply the number by its count in the right list
        # If the number doesn't exist in right list, count is 0
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score

def parse_input_file(filename):
    """
    Parse the input file containing two lists of numbers.
    
    Args:
        filename (str): Path to the input file
    
    Returns:
        tuple: A tuple containing left and right lists of numbers
    """
    try:
        with open(filename, 'r') as file:
            # Read lines and convert to lists of integers
            lines = file.readlines()
            
            # Split each line into numbers
            left_list = [int(line.split()[0]) for line in lines]
            right_list = [int(line.split()[1]) for line in lines]
            
            return left_list, right_list
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except (ValueError, IndexError):
        print("Error: Invalid input format. Each line should contain two space-separated numbers.")
        exit(1)

def main():
    import sys
    
    # Check if filename is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    # Get filename from command-line argument
    input_filename = sys.argv[1]
    
    # Parse input file
    left_list, right_list = parse_input_file(input_filename)
    
    # Calculate and print similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()
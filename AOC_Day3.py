import re
import sys

def extract_valid_multiplications(memory_string):
    """
    Extract valid multiplication instructions from corrupted memory.
    
    Args:
        memory_string (str): The corrupted memory string
    
    Returns:
        list: List of multiplication results
    """
    # Regex pattern to match valid mul() instructions
    # Looks for mul( followed by 1-3 digit numbers separated by a comma, then )
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid multiplications
    multiplications = re.findall(pattern, memory_string)
    
    # Calculate results of valid multiplications
    results = [int(x) * int(y) for x, y in multiplications]
    
    return results

def solve_memory_puzzle(filename):
    """
    Read corrupted memory from file and solve multiplication puzzle.
    
    Args:
        filename (str): Path to the input file
    
    Returns:
        int: Sum of multiplication results
    """
    try:
        # Read the entire file contents
        with open(filename, 'r') as file:
            memory_string = file.read().strip()
        
        # Extract and calculate multiplications
        results = extract_valid_multiplications(memory_string)
        
        # Return the sum of results
        return sum(results)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    # Check if filename is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    # Get filename from command-line argument
    input_filename = sys.argv[1]
    
    # Solve the memory puzzle
    result = solve_memory_puzzle(input_filename)
    
    # Print the result
    print(f"Sum of valid multiplications: {result}")

if __name__ == "__main__":
    main()
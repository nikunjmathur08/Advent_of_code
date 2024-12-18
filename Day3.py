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

import re
import sys

def parse_memory_instructions(memory_string):
    """
    Parse the corrupted memory, tracking multiplication enable/disable status
    
    Args:
        memory_string (str): The corrupted memory string
    
    Returns:
        list: List of multiplication results for enabled instructions
    """
    # Initialize multiplication status
    mul_enabled = True
    results = []
    
    # Regex patterns
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'?t\(\)'
    
    # Split the string to capture all instructions
    instructions = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'?t\(\))', memory_string)
    
    for instruction in instructions:
        # Check for do() instruction
        if re.match(do_pattern, instruction):
            mul_enabled = True
        
        # Check for don't() instruction
        elif re.match(dont_pattern, instruction):
            mul_enabled = False
        
        # Check for mul() instruction
        elif re.match(mul_pattern, instruction):
            # Only process if multiplication is currently enabled
            if mul_enabled:
                match = re.match(mul_pattern, instruction)
                x, y = map(int, match.groups())
                results.append(x * y)
    
    return results

def solve_memory_puzzle(filename):
    """
    Read corrupted memory from file and solve multiplication puzzle.
    
    Args:
        filename (str): Path to the input file
    
    Returns:
        int: Sum of enabled multiplication results
    """
    try:
        # Read the entire file contents
        with open(filename, 'r') as file:
            memory_string = file.read().strip()
        
        # Parse instructions and get multiplication results
        results = parse_memory_instructions(memory_string)
        
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
    print(f"Sum of enabled multiplications: {result}")

if __name__ == "__main__":
    main()
import os

def get_max_subsequence_value(bank_string, length_needed):
    digits = bank_string.strip()
    
    if len(digits) < length_needed:
        return 0
        
    result = []
    current_pos = 0 
    
    for i in range(length_needed):
        remaining_needed = length_needed - 1 - i
        
        search_limit = len(digits) - remaining_needed
        
        window = digits[current_pos : search_limit]
        
        best_digit = max(window)
        
        result.append(best_digit)
        
        current_pos += window.find(best_digit) + 1

    return int("".join(result))

def solve_puzzle():
    print("--- Battery Joltage Solver (Parts 1 & 2) ---")
    file_path = input("Please enter the path to your input file: ").strip()

    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]

    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} was not found.")
        return

    total_joltage_part1 = 0
    total_joltage_part2 = 0
    line_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    total_joltage_part1 += get_max_subsequence_value(line, 2)
                    total_joltage_part2 += get_max_subsequence_value(line, 12)
                    
                    line_count += 1
        
        print("-" * 40)
        print(f"Processed {line_count} battery banks.")
        print(f"Part 1 Total (2 digits):  {total_joltage_part1}")
        print(f"Part 2 Total (12 digits): {total_joltage_part2}")
        print("-" * 40)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve_puzzle()
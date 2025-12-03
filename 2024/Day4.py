def count_xmas_patterns(grid, rows, cols):
    count = 0
    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the X-MAS pattern can exist with (i, j) as the center
            if (i > 0 and i < rows - 1 and j > 0 and j < cols - 1):
                # Check the top-left and bottom-right 'M'
                if grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'M':
                    # Check the top-right and bottom-left 'S'
                    if grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'S':
                        # Check the center 'A'
                        if grid[i][j] == 'A':
                            count += 1
                # Check reversed MAS
                if grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'S':
                    if grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'M':
                        if grid[i][j] == 'A':
                            count += 1
    return count

def create_grid(input_string):
    # Split input into rows based on newline characters
    rows = input_string.strip().split('\n')
    grid = [list(row) for row in rows]
    return grid, len(grid), len(grid[0])

# Main function
def main():
    # Read input string from a file
    with open('day4.txt', 'r') as file:
        input_string = file.read()

    grid, rows, cols = create_grid(input_string)
    result = count_xmas_patterns(grid, rows, cols)
    print("Number of X-MAS patterns:", result)

if __name__ == "__main__":
    main()

import copy
input_file = open("day12.txt", "r")

grid = [list(line.strip()) for line in input_file.readlines()]
grid_copy = copy.deepcopy(grid)

# UP, RIGHT, DOWN, LEFT aka North, East, South, West
dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

def inbounds(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def edges(row, col):
    edges = 0
    plant = grid[row][col]
    for i in range(4):
        newR = row + dR[i]
        newC = col + dC[i]
        if not inbounds(newR,newC) or grid_copy[newR][newC] != plant:
            edges += 1
    return edges

def price_region(startRow, startCol):
    area = 1
    perimeter = edges(startRow, startCol)

    plant = grid[startRow][startCol]
    queue = [(startRow, startCol)]
    grid[startRow][startCol] = '#'

    while queue:
        row, col = queue.pop(0)

        for i in range(4):
            newR = row + dR[i]
            newC = col + dC[i]

            if inbounds(newR, newC) and grid[newR][newC] == plant:
                area += 1
                perimeter += edges(newR, newC)
                grid[newR][newC] = '#'
                queue.append((newR, newC))

    return area * perimeter

total_price = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '#':
            total_price += price_region(r, c)

print("Part 1 answer:", total_price)

grid = copy.deepcopy(grid_copy)

# Same idea as Part 1, but we want to deduplicate (not count) edges for sides that have already been counted
# We can do this by *only* counting edges for corner plants
# Ex: only count the top edge of the first A in AAAA
# (By always checking the plant to your left, to see if this top side has already been counted)
# You can rotate this strategy by 90 degress for every other direction too
# Lastly, add an extra check for the special "L-shape" concavity corner case
# Ex:  A
#      AA
# We actually do want to count the top edge for the last A, even though there *is* an A to its left.
# So you also need to check the (top-left) diagonal plant. Again, rotating the idea 90 degress for other sides

def sides(row, col):
    plant_sides = 0
    plant = grid[row][col]
    for i in range(4):
        newR = row + dR[i]
        newC = col + dC[i]
        if not inbounds(newR,newC) or grid_copy[newR][newC] != plant:
            newR_90CC = row + dR[(i - 1) % 4]
            newC_90CC = col + dC[(i - 1) % 4]
            isBeginEdge = not inbounds(newR_90CC, newC_90CC) or grid_copy[newR_90CC][newC_90CC] != plant

            newR_Corner = newR + dR[(i - 1) % 4]
            newC_Corner = newC + dC[(i - 1) % 4]
            isConcaveBeginEdge = inbounds(newR_Corner, newC_Corner) and grid_copy[newR_Corner][newC_Corner] == plant

            if isBeginEdge or isConcaveBeginEdge:
                plant_sides += 1

    return plant_sides

def price_region(startRow, startCol):
    area = 1
    region_sides = sides(startRow, startCol)

    plant = grid[startRow][startCol]
    queue = [(startRow, startCol)]
    grid[startRow][startCol] = '#'

    while queue:
        row, col = queue.pop(0)

        for i in range(4):
            newR = row + dR[i]
            newC = col + dC[i]

            if inbounds(newR, newC) and grid[newR][newC] == plant:
                area += 1
                region_sides += sides(newR, newC)
                grid[newR][newC] = '#'
                queue.append((newR, newC))

    return area * region_sides

total_price = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '#':
            total_price += price_region(r, c)

print("Part 2 answer:", total_price)
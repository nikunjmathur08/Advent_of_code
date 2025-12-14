import sys
from collections import defaultdict
import math

def parse_input(filename):
    """Parse the input file and return list of junction box coordinates."""
    boxes = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(','))
                boxes.append((x, y, z))
    return boxes

def distance(box1, box2):
    """Calculate Euclidean distance between two junction boxes."""
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

class UnionFind:
    """Union-Find data structure for tracking connected circuits."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        """Find the root of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        
        return True
    
    def get_circuit_sizes(self):
        """Get the sizes of all circuits."""
        circuit_sizes = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            circuit_sizes[root] = self.size[root]
        return list(circuit_sizes.values())

def solve(filename):
    """Solve the junction box connection problem."""
    boxes = parse_input(filename)
    n = len(boxes)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(boxes[i], boxes[j])
            edges.append((dist, i, j))
    
    edges.sort()
    uf = UnionFind(n)
    connections_made = 0
    for dist, i, j in edges:
        uf.union(i, j)
        connections_made += 1
        
        if connections_made >= 1000:
            break
    
    circuit_sizes = uf.get_circuit_sizes()
    circuit_sizes.sort(reverse=True)
    
    if len(circuit_sizes) >= 3:
        part1_result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    elif len(circuit_sizes) == 2:
        part1_result = circuit_sizes[0] * circuit_sizes[1] * 1
    elif len(circuit_sizes) == 1:
        part1_result = circuit_sizes[0] * 1 * 1
    else:
        part1_result = 0
    uf2 = UnionFind(n)
    last_connection = None
    
    for dist, i, j in edges:

        if uf2.find(i) != uf2.find(j):
            uf2.union(i, j)
            last_connection = (i, j)
            
            circuit_count = len(set(uf2.find(k) for k in range(n)))
            if circuit_count == 1:
                break
    
    if last_connection:
        i, j = last_connection
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        part2_result = x1 * x2
        
        return part1_result, part2_result
    
    return part1_result, None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    part1, part2 = solve(filename)
    print(f"Part 1 Answer: {part1}")
    if part2:
        print(f"Part 2 Answer: {part2}")
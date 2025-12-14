INPUT_FILE = "2025/day9.txt"

def part1():
    with open(INPUT_FILE, "r") as f:
        coords = [[int(n) for n in line.strip().split(",")] for line in f]

    area = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i+1, len(coords)):
            x2, y2 = coords[j]
            if x1 != x2 and y1 != y2:
                a = (abs(x1-x2)+1) * (abs(y1-y2)+1)
                area = max(area, a)
    print(area)


def part2():
    with open(INPUT_FILE, "r") as f:
        coords = [[int(n) for n in line.strip().split(",")] for line in f]

    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])

    # Vertical sweep
    spans = [None for y in range(max_y+2)]
    coords.append(coords[0])
    for i in range(1, len(coords)):
        x1, y1 = coords[i-1]
        x2, y2 = coords[i]
        if x1 > x2: x1,x2 = x2,x1
        if y1 > y2: y1,y2 = y2,y1
        for y in range(y1,y2+1):
            if spans[y] is None:
                spans[y] = [x1, x2]
            else:
                sx1, sx2 = spans[y]
                spans[y] = [min(x1, sx1), max(x2, sx2)]
    coords.pop()

    '''
    for y in range(max_y+2):
        if spans[y] is None:
            print("." * (max_x+2))
        else:
            sx1, sx2 = spans[y]
            print(f"{'.' * sx1}{'X' * (sx2-sx1+1)}{'.' * (max_x+1-sx2)}")
    return
    '''

    def rect_ok(x1, y1, x2, y2):
        if x1 > x2: x1,x2 = x2,x1
        if y1 > y2: y1,y2 = y2,y1
        for y in range(y1, y2+1):
            sx1, sx2 = spans[y]
            if x1 < sx1 or x1 > sx2 or x2 < sx1 or x2 > sx2:
                return False
        return True

    area = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i+1, len(coords)):
            x2, y2 = coords[j]
            if x1 != x2 and y1 != y2:
                a = (abs(x1-x2)+1) * (abs(y1-y2)+1)
                if a > area and rect_ok(x1, y1, x2, y2):
                    area = a
    print(area)

part1()
part2()
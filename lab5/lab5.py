from collections import deque

N = 8

with open('input.txt', 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    start = tuple(map(int, lines[1].split(',')))
    end = tuple(map(int, lines[2].split(',')))

directions_knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
directions_king = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
direction_pawn = [(1, 0)]
directions_queen = []
directions_rook = []
directions_bishop = []

def row_pos_append(list):
    i = 1
    while i <= N:
        list.append((i, 0))
        list.append((-i, 0))
        list.append((0, i))
        list.append((0, -i))
        i += 1
    return list

def lines_pos_append(list):
    i = 1
    while i <= N:
        list.append((i, -i))
        list.append((-i, i))
        list.append((-i, i))
        list.append((i, -i))
        i += 1
    return list

directions_rook = row_pos_append(directions_rook)
directions_queen = row_pos_append(directions_queen)
directions_queen = lines_pos_append(directions_queen)
directions_bishop = lines_pos_append(directions_bishop)

def min_moves(start, end, directions):
    if start == end:
        return 0
    
    queue = deque([(start[0], start[1], 0)])

    visited = {start}

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) == end:
                return dist + 1

            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                
    return "Шляху немає"

with open('output.txt', 'w') as f:
        f.write(str(min_moves(start, end, directions_knight)))

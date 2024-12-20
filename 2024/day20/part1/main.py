import math
from collections import Counter
from functools import reduce

debug = False

lines = open("big_input.txt").read().splitlines()

height = len(lines)
width = len(lines[0])

track = []
walls = []
grid = []
for line in lines:
    grid.append(list(line))

start = (0,0)
end = (width-1, height-1)

for r in range(height):
    for c in range(width):
        if grid[r][c] == 'S':
            start = (r,c)
        elif grid[r][c] == 'E':
            end = (r,c)
        elif grid[r][c] == '.':
            track.append((r,c))

if debug:
    for r in grid:
        print(''.join(r))
    print()

def a_star():
    open_set = set([start]) # TODO: check if 0,0 is corrupted?

    came_from = {}

    g_score = {start: 0}

    f_score = {start: h(start)}

    while open_set:
        current = min(open_set, key=f_score.get)
        #print('current: ', current)
        if current == end:
            return came_from
        open_set.remove(current)
        for neighbor in neighbors(current):
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor)
                open_set.add(neighbor)

    return None

def h(pos):
    return math.sqrt((pos[0]-width)**2 + (pos[1]-height)**2)

def neighbors(pos):
    the_neighbors = []

    if pos[0] < width-2:
        the_neighbors.append((pos[0]+1, pos[1]))
    if pos[1] < height-2:
        the_neighbors.append((pos[0], pos[1]+1))
    if pos[0] > 1:
        the_neighbors.append((pos[0]-1, pos[1]))
    if pos[1] > 1:
        the_neighbors.append((pos[0], pos[1]-1))

    return the_neighbors

def find_walls():
    walls = []
    for t in track:
        for r, c in neighbors(t):
            if grid[r][c] == '#':
                walls.append((r, c))
    return list(set(walls))
walls = find_walls()

def run_a_star():
    path_map = a_star()
    #print(path_map)

    path = set([start, end])

    curr = path_map[end]
    while curr != start:
        path.add(curr)
        curr = path_map[curr]

    if debug:
        for r in range(height):
            for c in range(width):
                if (c,r) in path:
                    print('O', end='')
                else:
                    print(grid[r][c], end='')
            print()
    return len(path)-1

base_picoseconds = run_a_star()
if debug:
    print("base", base_picoseconds)

saved_picoseconds_freqs = Counter()

for wall in walls:
    grid[wall[0]][wall[1]] = '.'

    saved_picoseconds = base_picoseconds - run_a_star()
    if saved_picoseconds >= 100:
        saved_picoseconds_freqs[saved_picoseconds] += 1

    grid[wall[0]][wall[1]] = '#'

if debug:
    print(sorted(saved_picoseconds_freqs.items()))
print(reduce(lambda x, y: x+y, saved_picoseconds_freqs.values(), 0))





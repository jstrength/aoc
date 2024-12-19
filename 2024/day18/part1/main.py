import math

lines = open("big_input.txt").read().splitlines()

width = 71
height = 71

bytes = []
for line in lines:
    bytes.append(tuple(map(int,line.split(","))))

grid = [['.' for _ in range(width)] for _ in range(height)]
for i in range(1024):
    grid[bytes[i][1]][bytes[i][0]] = '#'

for r in range(height):
    for c in range(width):
        print(grid[r][c], end='')
    print()

def a_star():
    start = (0,0)
    open_set = set([start]) # TODO: check if 0,0 is corrupted?

    came_from = {}

    g_score = {start: 0}

    f_score = {start: h(start)}

    while open_set:
        current = min(open_set, key=f_score.get)
        #print('current: ', current)
        if current == (width-1, height-1):
            return came_from
        open_set.remove(current)
        for neighbor in neighbors(current):
            if grid[neighbor[1]][neighbor[0]] == '#':
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

    if pos[0] < width-1:
        the_neighbors.append((pos[0]+1, pos[1]))
    if pos[1] < height-1:
        the_neighbors.append((pos[0], pos[1]+1))
    if pos[0] > 0:
        the_neighbors.append((pos[0]-1, pos[1]))
    if pos[1] > 0:
        the_neighbors.append((pos[0], pos[1]-1))

    return the_neighbors

path_map = a_star()
print(path_map)


path = set([(0,0), (width-1, height-1)])

curr = path_map[(width-1, height-1)]
while curr != (0,0):
    path.add(curr)
    curr = path_map[curr]

for r in range(height):
    for c in range(width):
        if (c,r) in path:
            print('O', end='')
        else:
            print(grid[r][c], end='')
    print()


print(len(path)-1)


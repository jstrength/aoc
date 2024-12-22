from collections import Counter

debug = False

lines = open("big_input.txt").read().splitlines()

height = len(lines)
width = len(lines[0])

grid = []
for line in lines:
    grid.append(list(line))

path = []
path_to_end = {}

for r in range(height):
    for c in range(width):
        if grid[r][c] == 'S':
            path.append((r,c))
            break
    if path:
        break

def print_grid():
    print("\033[%d;%dH" % (0, 1))
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')
        print()


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


def get_surrounding(pos):
    seen = set()
    q = [pos]
    q2 = []
    depth = 0
    nodes = {}

    while True:
        nodes[depth] = q.copy()
        while q:
            curr = q.pop(0)
            for neighbor in neighbors(curr):
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                q2.append(neighbor)

        depth += 1
        if q2 and depth < 20:
            q = q2
            q2 = []
        else:
            nodes[depth] = q2.copy()
            break

    return nodes

while True:
    for neighbor in neighbors(path[-1]):
        if grid[neighbor[0]][neighbor[1]] == 'E':
            path.append(neighbor)
            break
        if grid[neighbor[0]][neighbor[1]] == '.':
            if len(path) > 1 and neighbor == path[-2]:
                continue
            path.append(neighbor)
            break
    if grid[path[-1][0]][path[-1][1]] == 'E':
        break

for i in range(len(path)):
    path_to_end[path[i]] = len(path) - 1 - i

nanosecs_saved = Counter()
total_nanosecs_saved = 0
for curr in path:
    for depth, nodes in get_surrounding(curr).items():
        for p in nodes:
            if grid[p[0]][p[1]] == '.' or grid[p[0]][p[1]] == 'E':
                curr_nanosecs = path_to_end[curr] - path_to_end[p] - depth
                if curr_nanosecs >= 100:
                    nanosecs_saved[curr_nanosecs] += 1
                    total_nanosecs_saved += 1

print(sorted(nanosecs_saved.items()))
print(total_nanosecs_saved)
#  1146002 is too high

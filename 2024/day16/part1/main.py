import math

lines = open("big_input.txt").read().splitlines()

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

grid = []
start = (0,0)
goal = (0,0)
for r in range(len(lines)):
    row = []
    print(lines[r])
    for c in range(len(lines[0])):
        row.append(lines[r][c])
        if lines[r][c] == 'S':
            start = (r,c,LEFT)
        elif lines[r][c] == 'E':
            goal = (r,c,LEFT)
    grid.append(row)

print(start)
print(goal)

def a_start(start, goal, h):
    open_set = set([start])

    came_from = {}

    g_score = {start: 0}
    f_score = {start: h(start)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        open_set.remove(current)

        if current[:2] == goal[:2]:
            break

        for neighbor in neighbors(current):
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            tentative_g_score = g_score[current] + d(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                came_from[neighbor] = current
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return came_from, g_score

def neighbors(pos):
    r,c,_ = pos
    return [(r-1,c,UP),(r+1,c,DOWN),(r,c-1,LEFT),(r,c+1,RIGHT)]

def h(pos):
    return 1
    r,c = pos
    return math.sqrt(pow(r - goal[0], 2) + pow(c - goal[1], 2))

def d(curr_pos, next_pos):
    if curr_pos[2] != next_pos[2]:
        return 1001
    return 1

came_from, g_score = a_start(start, goal, h)

print(came_from)
goal = (goal[0], goal[1], UP)
path = set([goal])
path2 = [goal]
curr = goal
while curr != start:
    curr = came_from[curr]
    path.add((curr[0], curr[1]))
    path2.append(curr)
print(path)


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r,c) in path:
            print('*', end='')
        else:
            print(grid[r][c], end='')
    print()

path2.reverse()
for p in path2:
    print(p, " : ", g_score[p], end=' -> ')
print()

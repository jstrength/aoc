from collections import defaultdict
from pprint import pprint
import os, time

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
    #print(lines[r])
    for c in range(len(lines[0])):
        row.append(lines[r][c])
        if lines[r][c] == 'S':
            start = (r,c,LEFT)
        elif lines[r][c] == 'E':
            goal = (r,c,LEFT)
    grid.append(row)

#print(start)
#print(goal)

def a_star(start, goal):
    open_set = set([start])
    came_from = defaultdict(list)
    g_score = {start: 0}

    while open_set:
        current = min(open_set, key=lambda x: g_score[x])
        open_set.remove(current)

        if current[:2] == goal[:2]:
            break

        for neighbor in neighbors(current):
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            tentative_g_score = g_score[current] + d(current, neighbor)
            if neighbor not in g_score or tentative_g_score <= g_score[neighbor]:
                if neighbor in g_score and tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = [current]
                else:
                    came_from[neighbor].append(current)
                g_score[neighbor] = tentative_g_score
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return came_from, g_score

def neighbors(pos):
    r,c,_ = pos
    return [(r-1,c,UP),(r+1,c,DOWN),(r,c-1,LEFT),(r,c+1,RIGHT)]

def d(curr_pos, next_pos):
    if curr_pos[2] != next_pos[2]:
        return 1001
    return 1

def h(pos):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def print_grid(path):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[%d;%dH" % (0, 1))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r,c) in path:
                print('O', end='')
            else:
                print(grid[r][c], end='')
        print()
    time.sleep(0.1)


came_from, g_score = a_star(start, goal)

#pprint(came_from)
path = set([(goal[0], goal[1])])
q = [(goal[0], goal[1], UP), (goal[0], goal[1], DOWN), (goal[0], goal[1], LEFT), (goal[0], goal[1], RIGHT)]
#q = [(goal[0], goal[1], RIGHT)]
min_scores = [g_score[next_curr] if next_curr in g_score else float('inf') for next_curr in q]
if len(min_scores) >= 1:
    min_score = min(min_scores)
else:
    min_score = 0
q = list(filter(lambda x: x in g_score and g_score[x] == min_score, q))
seen = set()
#os.system('cls' if os.name == 'nt' else 'clear')
while q:
    curr = q.pop(0)
    if curr in seen:
        continue
    seen.add(curr)
    if curr not in came_from:
        continue
    next_list = came_from[curr]
    if not next_list:
        continue
    #if len(next_list) > 1:
    #    print("FOUND")
    #    print(curr, next_list)
    #min_scores = []
    #for next_curr in next_list:
    #    if next_curr in g_score:
    #        min_scores += g_score[next_curr]
    #print(min_scores)
    #min_score = min(min_scores)
    #print(min_score)
    for next_curr in next_list:
        found = False
        #for score in g_score[next_curr]:
        #    if score == min_score:
        #        found = True
        #        break
        #if not found:
        #    continue
        q.append(next_curr)
        path.add((next_curr[0], next_curr[1]))
        #print_grid(path)
        #print(min_scores)
        #time.sleep(1)
        #input()
#print(path)


#print_grid(path)
print(len(path))
#686 too high
#592 too low


#os.system('cls' if os.name == 'nt' else 'clear')
exit()
q = [(goal[0], goal[1], UP), (goal[0], goal[1], DOWN), (goal[0], goal[1], LEFT), (goal[0], goal[1], RIGHT)]
seen = set()
path = []

while q:
    curr = q.pop(0)
    if curr in seen:
        continue
    seen.add(curr)
    next_list = came_from[curr]
    if not next_list:
        continue
    for next_curr in next_list:
        q.append(next_curr)
    path.append((curr[0], curr[1]))
    print_grid(path)





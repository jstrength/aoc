lines = open("big_input.txt").readlines()

grid = []

for line in lines:
    line = line.strip()
    grid.append(list(line))

curr_pos = (0, 0)

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "^":
            curr_pos = (r, c)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
dir = UP

while True:
    grid[curr_pos[0]][curr_pos[1]] = "X"
    if dir == UP:
        if curr_pos[0] == 0:
            break
        if grid[curr_pos[0] - 1][curr_pos[1]] == "#":
            dir = RIGHT
            continue
        grid[curr_pos[0] - 1][curr_pos[1]] = "X"
        curr_pos = (curr_pos[0] - 1, curr_pos[1])
    elif dir == RIGHT:
        if curr_pos[1] == len(grid[0]) - 1:
            break
        if grid[curr_pos[0]][curr_pos[1] + 1] == "#":
            dir = DOWN
            continue
        grid[curr_pos[0]][curr_pos[1] + 1] = "X"
        curr_pos = (curr_pos[0], curr_pos[1] + 1)
    elif dir == DOWN:
        if curr_pos[0] == len(grid) - 1:
            break
        if grid[curr_pos[0] + 1][curr_pos[1]] == "#":
            dir = LEFT
            continue
        grid[curr_pos[0] + 1][curr_pos[1]] = "X"
        curr_pos = (curr_pos[0] + 1, curr_pos[1])
    else:
        if curr_pos[1] == 0:
            break
        if grid[curr_pos[0]][curr_pos[1] - 1] == "#":
            dir = UP
            continue
        grid[curr_pos[0]][curr_pos[1] - 1] = "X"
        curr_pos = (curr_pos[0], curr_pos[1] - 1)

distinct_position = 0
for r in grid:
    for c in r:
        if c == "X":
            distinct_position += 1

#print(curr_pos)
#for r in grid:
#    print(r)
print(distinct_position)

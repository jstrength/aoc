from pprint import pprint

raw_grids = open("big_input.txt").read().strip().split("\n\n")

grids = []
keys = []
locks = []

for raw_grid in raw_grids:
    grids.append(raw_grid.split("\n"))

for grid in grids:
    if grid[0][0] == "#":
        curr_key = []
        for j in range(len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == "#":
                    count += 1
            curr_key.append(count-1)
        locks.append(curr_key)
    else:
        curr_key = []
        for j in range(len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == "#":
                    count += 1
            curr_key.append(count-1)
        keys.append(curr_key)


count = 0
for key in keys:
    for lock in locks:
        bad = False
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                bad = True
                break
        if not bad:
            count += 1

print(count)

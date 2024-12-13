from collections import defaultdict

lines = open('big_input.txt').read().splitlines()

regions = defaultdict(set)

grid = [[x for x in line] for line in lines]

#print(grid)

curr = (0,0)

seen = set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r,c) in seen:
            continue

        q = [(r,c)]
        while q:
            curr = q.pop(0)
            if curr in seen:
                continue

            seen.add((curr[0], curr[1]))
            regions[(grid[r][c]), (r,c)].add((curr[0], curr[1]))

            for rx, cx in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr = curr[0] + rx
                cc = curr[1] + cx

                if rr < 0 or rr >= len(grid) or cc < 0 or cc >= len(grid[0]):
                    continue

                if grid[rr][cc] == grid[r][c]:
                    q.append((rr,cc))

#print(regions)

price = 0

for k, v in regions.items():
    area = len(v)
    sides = 0

    for (r,c) in v:

        north_exists = (r-1,c) in v
        south_exists = (r+1,c) in v
        east_exists = (r,c+1) in v
        west_exists = (r,c-1) in v
        northwest_exists = (r-1,c-1) in v
        northeast_exists = (r-1,c+1) in v
        southeast_exists = (r+1,c+1) in v
        southwest_exists = (r+1,c-1) in v

        #top right corner
        if not northeast_exists:
            if north_exists and east_exists or not (north_exists or east_exists):
                sides += 1
        else:
            if not north_exists and not east_exists:
                sides += 1
        #top left corner
        if not northwest_exists:
            if north_exists and west_exists or not (north_exists or west_exists):
                sides += 1
        else:
            if not north_exists and not west_exists:
                sides += 1
        #bottom right corner
        if not southeast_exists:
            if south_exists and east_exists or not (south_exists or east_exists):
                sides += 1
        else:
            if not south_exists and not east_exists:
                sides += 1
        #bottom left corner
        if not southwest_exists:
            if south_exists and west_exists or not (south_exists or west_exists):
                sides += 1
        else:
            if not south_exists and not west_exists:
                sides += 1

    #print(k, area, sides, area*sides)

    price += area*sides

print(price)

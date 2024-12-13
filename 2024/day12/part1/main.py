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
    parameter = 0

    for (r,c) in v:
        curr_parameter = 4

        for (rr, cc) in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if (rr,cc) in v:
                curr_parameter -= 1

        parameter += curr_parameter

    #print(k, area, parameter, area*parameter)

    price += area*parameter

print(price)

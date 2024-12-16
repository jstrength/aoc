#lines = open('input.txt').read().splitlines()
#width = 11
#height = 7

lines = open('big_input.txt').read().splitlines()
width = 101
height = 103

robots = []
for line in lines:
    parts = line.split(" ")
    pos = list(map(int, parts[0].split("=")[1].split(",")))
    vel =  list(map(int, parts[1].split("=")[1].split(",")))
    robots.append({
        'pos': pos,
        'vel': vel,
    })


def print_grid():
    grid = [['.' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        x = robot['pos'][0]
        y = robot['pos'][1]
        if grid[y][x] != '.':
            grid[y][x] = str(int(grid[y][x]) + 1)
        else:
            grid[y][x] = '1'

    for row in grid:
        print(''.join(row))
    print()

def find_tree(idx):
    seen = set()
    groups = []
    robots_pos = set([tuple(r['pos']) for r in robots])
    #might need to count contiguous row location
    for robot in robots:
        q = [tuple(robot['pos'])]
        count = 0
        while q:
            curr = q.pop()
            if curr in seen:
                continue
            seen.add(curr)
            count += 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = (curr[0] + dx) % width
                y = (curr[1] + dy) % height
                if (x, y) not in seen and (x, y) in robots_pos:
                    q.append((x, y))
        groups.append(count)


    for g in groups:
        if g > 50:
            print_grid()
            print("Tree found after " + str(idx) + " seconds")
            return True

    return False

i = 0
while True:
    i += 1
    for robot in robots:
        robot['pos'][0] = (robot['pos'][0] + robot['vel'][0]) % width
        robot['pos'][1] = (robot['pos'][1] + robot['vel'][1]) % height
    if find_tree(i):
        break



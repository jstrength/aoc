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

    for y in range(height):
        for x in range(width):
            if x == width//2 or y == height//2:
                grid[y][x] = ' '
            print(grid[y][x], end='')
        print()

for _ in range(100):
    for robot in robots:
        robot['pos'][0] = (robot['pos'][0] + robot['vel'][0]) % width
        robot['pos'][1] = (robot['pos'][1] + robot['vel'][1]) % height

#print_grid()

#count quandrents
count = 1
quadrents = [0,0,0,0]
for robot in robots:
    x = robot['pos'][0]
    y = robot['pos'][1]
    if x < width//2 and y < height//2:
        quadrents[0] += 1
    elif x < width//2 and y > height//2:
        quadrents[1] += 1
    elif x > width//2 and y < height//2:
        quadrents[2] += 1
    elif x > width//2 and y > height//2:
        quadrents[3] += 1

for quadrent in quadrents:
    count *= quadrent
print(count)

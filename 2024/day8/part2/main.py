import math

lines = open('big_input.txt').readlines()

height = len(lines)
width = len(lines[0].strip())
print(height, width)

nodes = {}
antenna_count = 0
for r in range(len(lines)):
    lines[r] = lines[r].strip()
    for c in range(len(lines[r])):
        if lines[r][c] != '.':
            antenna_count += 1
            if lines[r][c] in nodes:
                nodes[lines[r][c]].append((r, c))
            else:
                nodes[lines[r][c]] = [(r, c)]
    print(lines[r])

def euclidean_distance(node1, node2):
    return round(math.sqrt(pow(node1[0] - node2[0], 2) + pow(node1[1] - node2[1], 2)))

antinodes = []
print(nodes)
for k, v in nodes.items():
    distances = []
    print(k, v)
    for i in range(len(v)):
        node1 = v[i]
        for j in range(i + 1, len(v)):
            node2 = v[j]
            print('node1', node1)
            print('node2', node2)
            y_dist = node1[0] - node2[0]
            x_dist = node1[1] - node2[1]
            print('x_dist1', x_dist)
            print('y_dist1', y_dist)
            distances.append(euclidean_distance(node1, node2))
            curr = node1
            while curr[0]+y_dist >= 0 and curr[1]+x_dist >= 0 and curr[0]+y_dist < height and curr[1]+x_dist < width:
                next = (curr[0]+y_dist, curr[1]+x_dist)
                print('adding', next)
                antinodes.append(next)
                curr = next

            y_dist = node2[0] - node1[0]
            x_dist = node2[1] - node1[1]
            print('x_dist2', x_dist)
            print('y_dist2', y_dist)
            curr = node2
            while curr[0]+y_dist >= 0 and curr[1]+x_dist >= 0 and curr[0]+y_dist < height and curr[1]+x_dist < width:
                next = (curr[0]+y_dist, curr[1]+x_dist)
                print('adding', next)
                antinodes.append(next)
                curr = next
    print(distances)

count = 0
for r in range(len(lines)):
    lines[r] = lines[r].strip()
    for c in range(len(lines[r])):
        if lines[r][c] != '.':
            print(lines[r][c], end='')
            continue
        found = False
        for (y,x) in antinodes:
            if (y, x) == (r, c):
                found = True
                count += 1
                print('#', end='')
                break
        if not found:
            print(lines[r][c], end='')
    print()

print(count)
print(len(set(antinodes)))
print(antenna_count)
print(len(set(antinodes)) + antenna_count)
print(count + antenna_count)
lines = open("big_input.txt").readlines()

topo_map = []
for line in lines:
    #topo_map.append(list(map(int, line.strip())))
    topo_map.append([int(x) if x != "." else -1 for x in line.strip()])

trailheads = []

for r in range(len(topo_map)):
    for c in range(len(topo_map[r])):
        if topo_map[r][c] == 0:
            trailheads.append((r, c))

def score_trailhead(trailhead):
    count = 0
    r, c = trailhead
    if topo_map[r][c] == 9:
        return 1

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r = r + dr
        new_c = c + dc

        if new_r < 0 or new_r >= len(topo_map):
            continue

        if new_c < 0 or new_c >= len(topo_map[0]):
            continue

        if topo_map[new_r][new_c] <= topo_map[r][c]:
            continue

        if topo_map[new_r][new_c] == topo_map[r][c] + 1:
            count += score_trailhead((new_r, new_c))

    return count

total = 0
for trailhead in trailheads:
    curr_score = score_trailhead(trailhead)
    #print(curr_score)
    total += curr_score

print(total)

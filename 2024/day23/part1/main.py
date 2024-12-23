from pprint import pprint 
from collections import defaultdict

lines = open("big_input.txt").read().splitlines()

connections = defaultdict(set)

for line in lines:
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)

three_groups = set()

for k1, vs1 in connections.items():
    for v1 in vs1:
        commons = vs1 & connections[v1]
        for v2 in commons:
            if k1[0] == 't' or v1[0] == 't' or v2[0] == 't':
                grouping = tuple(sorted([k1, v1, v2]))
                three_groups.add(grouping)

#pprint(sorted(list(three_groups)))
print(len(three_groups))

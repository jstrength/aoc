from pprint import pprint 
from collections import defaultdict

lines = open("big_input.txt").read().splitlines()

connections = defaultdict(set)

for line in lines:
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)

groupings = []

def find_grouping(curr_grouping):
    for k, vs in connections.items():
        commons = curr_grouping & vs
        if commons == curr_grouping:
            return find_grouping(commons | {k})

    return curr_grouping


for k1, vs1 in connections.items():
    groupings.append(find_grouping(set([k1])))

largest_group = []
for grouping in groupings:
    if len(grouping) > len(largest_group):
        largest_group = grouping

#pprint(sorted(list(groupings)))
#print(len(groupings))
largest_group = sorted(largest_group)
print(','.join(largest_group))

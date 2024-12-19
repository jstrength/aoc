from collections import defaultdict

raw_towel_patterns, raw_designs = open("big_input.txt").read().split("\n\n")

towel_patterns = raw_towel_patterns.split(", ")
designs = raw_designs.strip().split("\n")

cache = defaultdict(int)
def count_sort(design, idx):
    if design[idx:] in cache:
        return cache[design[idx:]]

    count = 0
    if idx == len(design):
        return 1
    for pattern in towel_patterns:
        if design[idx:idx+len(pattern)] == pattern:
            count += count_sort(design, idx+len(pattern))
    cache[design[idx:]] = count
    return count

total_count = 0
for design in designs:
    #print(design)
    total_count += count_sort(design, 0)
    #print()

#print(cache)
print(total_count)

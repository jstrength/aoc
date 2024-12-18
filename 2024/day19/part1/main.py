raw_towel_patterns, raw_designs = open("big_input.txt").read().split("\n\n")

towel_patterns = raw_towel_patterns.split(", ")
designs = raw_designs.strip().split("\n")

cache = {}
def can_sort(design, idx):
    if design[idx:] in cache:
        return cache[design[idx:]]
    cache[design[:idx]] = True

    if idx == len(design):
        return True
    for pattern in towel_patterns:
        if design[idx:idx+len(pattern)] == pattern:
            if can_sort(design, idx+len(pattern)):
                return True
    cache[design[idx:]] = False
    return False

count = 0
for design in designs:
    #print(design)
    if can_sort(design, 0):
        count += 1 
    #print()

#print(cache)
print(count)

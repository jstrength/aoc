input = open("big_input.txt", "r").read()
# 15731241096934 too high

compacted_memory = list(map(int, input.strip()))
id = 0
expanded_memory = []
for i in range(len(compacted_memory)):
    if i % 2 == 0:
        for j in range(compacted_memory[i]):
            expanded_memory.append(str(id))
        id += 1
    else:
        for j in range(compacted_memory[i]):
            expanded_memory.append('.')
#print(''.join(expanded_memory))

p1 = 0
p2 = len(expanded_memory) - 1

def find_next_free_space(start, memory):
    p1 = -1
    for i in range(start, len(memory)):
        if memory[i] == '.':
            if p1 == -1:
                p1 = i
        elif p1 != -1:
            return (p1, i-1)
    return None

def find_next_file_number_space(start, memory):
    p1 = -1
    for i in range(start, -1, -1):
        if memory[i] != '.':
            if p1 == -1:
                p1 = i
        if p1 != -1 and memory[p1] != memory[i]:
            return (i+1, p1)
    return None

free_space_size = 0
i = 0
file_number_start = len(expanded_memory)-1
while True:
    i+=1
    free_space = find_next_free_space(0, expanded_memory)
    file_space = find_next_file_number_space(file_number_start, expanded_memory)

    if not file_space or expanded_memory[file_space[0]] == 0:
        break
    found = True

    while free_space[1]-free_space[0] < file_space[1]-file_space[0]:
        free_space = find_next_free_space(free_space[1]+1, expanded_memory)
        if not free_space:
            file_space = find_next_file_number_space(file_space[0]-1, expanded_memory)
            free_space = find_next_free_space(0, expanded_memory)
            if not file_space:
                found = False
                break

    if not found or free_space[1] > file_space[0]:
        file_number_start = file_space[0]-1
        continue

    if free_space[1]-free_space[0] >= file_space[1]-file_space[0]:
        #print('free_space', free_space)
        #print(expanded_memory[free_space[0]:free_space[1]+1])
        #print('file_space', file_space)
        #print(expanded_memory[file_space[0]:file_space[1]+1])
        expanded_memory[free_space[0]:free_space[0]+(file_space[1]-file_space[0]+1)] = expanded_memory[file_space[0]:file_space[1]+1]
        expanded_memory[file_space[0]:file_space[1]+1] = '.'*(file_space[1]-file_space[0]+1)
        file_number_start = file_space[0]-1
        #print(''.join(expanded_memory))


checksum = 0
for i in range(len(expanded_memory)):
    if expanded_memory[i] != '.':
        checksum += i*int(expanded_memory[i])
print(checksum)

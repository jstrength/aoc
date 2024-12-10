input = open("big_input.txt", "r").read()

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

while p1 < p2:
    if expanded_memory[p1] != '.':
        p1 += 1
        continue
    if expanded_memory[p2] == '.':
        p2 -= 1
        continue
    tmp = expanded_memory[p1]
    expanded_memory[p1] = expanded_memory[p2]
    expanded_memory[p2] = tmp
    p1 += 1
    p2 -= 1
    #print(''.join(expanded_memory))

checksum = 0
for i in range(len(expanded_memory)):
    if expanded_memory[i] != '.':
        checksum += i*int(expanded_memory[i])
print(checksum)

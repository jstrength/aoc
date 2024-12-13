stones = open('big_input.txt').read().strip().split()

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stones.append(str(int(stone)*2024))
    stones = new_stones
    #print(stones)

print(len(stones))

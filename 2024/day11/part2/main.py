stones = open('big_input.txt').read().strip().split()

memo = {}

def calc_new_stones(stone, iter):
    if iter == 0:
        return 1

    count = 1
    if (iter,stone) not in memo:
        if stone == '0':
            count = calc_new_stones('1', iter-1)
        elif len(stone) % 2 == 0:
            count = calc_new_stones(str(int(stone[:len(stone)//2])), iter-1) + \
                calc_new_stones(str(int(stone[len(stone)//2:])), iter-1)
        else:
            count = calc_new_stones(str(int(stone)*2024), iter-1)

        memo[(iter, stone)] = count
    else:
        count = memo[(iter,stone)]

    return count

stone_count = 0
for stone in stones:
    stone_count += calc_new_stones(stone, 75)
#stones = new_stones
#print(stones)

#print(memo)
print(stone_count)

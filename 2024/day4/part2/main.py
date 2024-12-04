lines = open("big_input.txt").read().splitlines()

depth = len(lines)
width = len(lines[0])

x_mas = "MAS"

def check_x_mas(r, c):
    word = ''
    if r-1 >= 0 and c-1 >= 0:
        word += lines[r-1][c-1]
    word += 'A'
    if r+1 < depth and c+1 < width:
        word += lines[r+1][c+1]
    if word != x_mas and word[::-1] != x_mas:
        return False

    word = ''
    if r+1 < depth and c-1 >= 0:
        word += lines[r+1][c-1]
    word += 'A'
    if r-1 >= 0 and c+1 < width:
        word += lines[r-1][c+1]
    if word != x_mas and word[::-1] != x_mas:
        return False

    return True

xmas_count = 0

for r in range(depth):
    for c in range(width):
        if lines[r][c] == "A":
            if check_x_mas(r, c):
                xmas_count += 1

print(xmas_count)

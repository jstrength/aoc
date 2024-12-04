lines = open("big_input.txt").read().splitlines()

depth = len(lines)
width = len(lines[0])

xmas = "XMAS"

def count_diagonals(r, c):
    count = 0

    word = ''
    for i in range(4):
        if r-i < 0 or c-i < 0:
            break
        word += lines[r-i][c-i]
    if word == xmas:
        count += 1

    word = ''
    for i in range(4):
        if r+i >= depth or c+i >= width:
            break
        word += lines[r+i][c+i]
    if word == xmas:
        count += 1

    word = ''
    for i in range(4):
        if r-i < 0 or c+i >= width:
            break
        word += lines[r-i][c+i]
    if word == xmas:
        count += 1

    word = ''
    for i in range(4):
        if r+i >= depth or c-i < 0:
            break
        word += lines[r+i][c-i]
    if word == xmas:
        count += 1

    return count

def count_perpendicular(r, c):
    count = 0
    if lines[r][c:c+4] == xmas:
        count += 1
    if lines[r][c-3:c+1] == xmas[::-1]:
        count += 1

    word = ''
    for i in range(4):
        if r-i < 0:
            break
        word += lines[r-i][c]
    if word == xmas:
        count += 1

    word = ''
    for i in range(4):
        if r+i >= depth:
            break
        word += lines[r+i][c]
    if word == xmas:
        count += 1

    return count

xmas_count = 0

for r in range(depth):
    for c in range(width):
        if lines[r][c] == "X":
            xmas_count += count_diagonals(r, c)
            xmas_count += count_perpendicular(r, c)

print(xmas_count)

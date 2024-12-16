lines = open('big_input.txt').read()

raw_grid, raw_moves = lines.split('\n\n')

grid = [list(grid_row) for grid_row in raw_grid.split('\n')]
moves = list(filter(lambda x: x != '\n', raw_moves))

start_pos = (0, 0)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            start_pos = (r, c)


def print_grid():
    for row in grid:
        print(''.join(row))
    print()

def move_up(pos):
    return (pos[0] - 1, pos[1])
def move_down(pos):
    return (pos[0] + 1, pos[1])
def move_left(pos):
    return (pos[0], pos[1] - 1)
def move_right(pos):
    return (pos[0], pos[1] + 1)

def step(move, curr_pos):
    curr_char = grid[curr_pos[0]][curr_pos[1]]
    move_fn = None
    match move:
        case '^':
            move_fn = move_up
        case 'v':
            move_fn = move_down
        case '>':
            move_fn = move_right
        case '<':
            move_fn = move_left

    next_pos = move_fn(curr_pos)
    if grid[next_pos[0]][next_pos[1]] == '#':
        return curr_pos
    elif grid[next_pos[0]][next_pos[1]] == 'O':
        tmp_next_post = step(move, next_pos)
        if tmp_next_post == next_pos:
            return curr_pos
        return step(move, curr_pos)
        #positions = []
        #curr = next_pos
        #while grid[curr[0]][curr[1]] != '.' and grid[curr[0]][curr[1]] != '#':
        #    positions.append(curr)
        #    curr = move_fn(curr)
        #if grid[curr[0]][curr[1]] == '#':
        #    return curr_pos
        #for pos in positions:
        #    grid[pos[0]][pos[1]] = '@'

    grid[curr_pos[0]][curr_pos[1]] = '.'
    curr_pos = next_pos
    grid[curr_pos[0]][curr_pos[1]] = curr_char
    return curr_pos

#print_grid()
def run(curr_pos):
    for move in moves:
        #print(move)
        curr_pos = step(move, curr_pos)
        #print_grid()

run(start_pos)
#print_grid()

gps_score = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            gps_score += 100 * r + c
print(gps_score)

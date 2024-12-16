import os, time

lines = open('big_input.txt').read()

raw_grid, raw_moves = lines.split('\n\n')

os.system('cls' if os.name == 'nt' else 'clear')
def print_grid():
    print("\033[%d;%dH" % (0, 1))
    for row in grid:
        print(''.join(row))
    print()
    time.sleep(0.001)
    #os.system('cls' if os.name == 'nt' else 'clear')

grid = [list(grid_row) for grid_row in raw_grid.split('\n')]
moves = list(filter(lambda x: x != '\n', raw_moves))

expanded_grid = []
for r in range(len(grid)):
    row = []
    for c in range(len(grid[0])):
        match grid[r][c]:
            case '@':
                row.append('@')
                row.append('.')
            case 'O':
                row.append('[')
                row.append(']')
            case _:
                row.append(grid[r][c])
                row.append(grid[r][c])
    expanded_grid.append(row)

grid = expanded_grid

start_pos = (0, 0)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            start_pos = (r, c)


def move_up(pos):
    return (pos[0] - 1, pos[1])
def move_down(pos):
    return (pos[0] + 1, pos[1])
def move_left(pos):
    return (pos[0], pos[1] - 1)
def move_right(pos):
    return (pos[0], pos[1] + 1)

def get_all_boxes(move_fn, curr_pos):
    boxes = []
    seen = set()
    q = [curr_pos]
    while q:
        curr = q.pop(0)
        if curr in seen:
            continue
        seen.add(curr)
        if grid[curr[0]][curr[1]] == '[':
            boxes.append(curr)
            q.append((curr[0], curr[1] + 1))
        elif grid[curr[0]][curr[1]] == ']':
            boxes.append(curr)
            q.append((curr[0], curr[1] - 1))
        elif grid[curr[0]][curr[1]] == '#':
            return []
        if grid[curr[0]][curr[1]] == '[' or grid[curr[0]][curr[1]] == ']':
            q.append(move_fn(curr))
    return boxes

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
    elif grid[next_pos[0]][next_pos[1]] == '[' or grid[next_pos[0]][next_pos[1]] == ']':
        boxes = get_all_boxes(move_fn, next_pos)
        #print(boxes)
        if not boxes:
            return curr_pos
        tmp_box_values_dict = {}
        for box in boxes:
            tmp_box_values_dict[box] = grid[box[0]][box[1]]
            grid[box[0]][box[1]] = '.'
        for box in boxes:
            box_next_pos = move_fn(box)
            grid[box_next_pos[0]][box_next_pos[1]] = tmp_box_values_dict[box]

    grid[curr_pos[0]][curr_pos[1]] = '.'
    curr_pos = next_pos
    grid[curr_pos[0]][curr_pos[1]] = curr_char
    return curr_pos

print_grid()
def run(curr_pos):
    for move in moves:
        #print(move)
        curr_pos = step(move, curr_pos)
        print_grid()
print_grid()

run(start_pos)

gps_score = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '[':
            gps_score += 100 * r + c
print(gps_score)

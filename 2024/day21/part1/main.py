codes = open("big_input.txt").read().splitlines()


### KEYPAD STUFF START ###
num_keypad = [
    ['7',  '8', '9'],
    ['4',  '5', '6'],
    ['1',  '2', '3'],
    [None, '0', 'A'],
]

num_keypad_cache = {}
num_keypad_to_pos = {}

for r in range(len(num_keypad)):
    for c in range(len(num_keypad[0])):
        if r == 3 and c == 0:
            continue
        num_keypad_to_pos[num_keypad[r][c]] = (r, c)

def calc_num_keypad_shortest_path(src, dest):
    q = [(src, '')]
    solutions = []

    while q:
        pos, path = q.pop(0)
        if solutions and len(solutions[0]) <= len(path):
            continue

        if pos[0] < 0 or pos[0] > len(num_keypad)-1 or pos[1] < 0 or pos[1] > len(num_keypad[0])-1 or \
            (pos[0] == len(num_keypad)-1 and pos[1] == 0):
            continue

        if pos == dest:
            solutions.append(path + 'A')
            continue

        q.append(((pos[0]-1, pos[1]), path + '^'))
        q.append(((pos[0], pos[1]-1), path + '<'))
        q.append(((pos[0]+1, pos[1]), path + 'v'))
        q.append(((pos[0], pos[1]+1), path + '>'))

    return solutions


def build_num_keypad_cache():
    positions = set()
    for r in range(len(num_keypad)):
        for c in range(len(num_keypad[0])):
            if r == 3 and c == 0:
                continue
            positions.add((r, c))
    for src in positions:
        for dest in positions:
            num_keypad_cache[(src, num_keypad[dest[0]][dest[1]])] = calc_num_keypad_shortest_path(src, dest)

### KEYPAD STUFF END ###

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]

dir_keypad_cache = {}
dir_keypad_to_pos = {}

for r in range(len(dir_keypad)):
    for c in range(len(dir_keypad[0])):
        if r == 0 and c == 0:
            continue
        dir_keypad_to_pos[dir_keypad[r][c]] = (r, c)


def calc_dir_keypad_shortest_path(src, dest):
    q = [(src, '')]
    solutions = []

    while q:
        pos, path = q.pop(0)
        if solutions and len(solutions[0]) <= len(path):
            continue

        if pos[0] < 0 or pos[0] > len(dir_keypad)-1 or pos[1] < 0 or pos[1] > len(dir_keypad[0])-1 or \
            (pos[0] == 0 and pos[1] == 0):
            continue

        if pos == dest:
            solutions.append(path + 'A')
            continue

        q.append(((pos[0]-1, pos[1]), path + '^'))
        q.append(((pos[0], pos[1]-1), path + '<'))
        q.append(((pos[0]+1, pos[1]), path + 'v'))
        q.append(((pos[0], pos[1]+1), path + '>'))

    return solutions

def build_dir_keypad_cache():
    positions = set()
    for r in range(len(dir_keypad)):
        for c in range(len(dir_keypad[0])):
            if r == 0 and c == 0:
                continue
            positions.add((r, c))
    for src in positions:
        for dest in positions:
            dir_keypad_cache[(src, dir_keypad[dest[0]][dest[1]])] = calc_dir_keypad_shortest_path(src, dest)

build_num_keypad_cache()
build_dir_keypad_cache()

def run_robot_robot(robot_count, code):
    final_path = ''
    pos = dir_keypad_to_pos['A']

    for c in code:
        min_path = ''
        for path in dir_keypad_cache[(pos, c)]:
            if robot_count == 1:
                min_path = path
                break
            curr_path = run_robot_robot(robot_count-1, path)
            if min_path == '' or len(curr_path) < len(min_path):
                min_path = curr_path
        final_path += min_path
        pos = dir_keypad_to_pos[c]

    return final_path


def run_robot(code):
    final_path = ''
    num_pos = num_keypad_to_pos['A']
    for c in code:
        paths = num_keypad_cache[(num_pos, c)]
        num_pos = num_keypad_to_pos[c]

        min_path = ''
        for path in paths:
            curr_path = run_robot_robot(2, path)
            if min_path == '' or len(curr_path) < len(min_path):
                min_path = curr_path

        final_path += min_path
    return final_path

complexity_score = 0
for code in codes:
    #print(code)
    curr_path = run_robot(code)
    #print(curr_path)
    #print(len(curr_path), int(code.replace('A', '')))
    complexity_score += len(curr_path) * int(code.replace('A', ''))

print(complexity_score)


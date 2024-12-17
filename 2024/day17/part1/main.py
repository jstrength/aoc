lines = open("big_input.txt").read()

ip = 0
registers = {
    'A': 0,
    'B': 0,
    'C': 0
}
output = []

raw_registers_input, raw_program_input = lines.split("\n\n")

raw_registers = raw_registers_input.split('\n')
registers['A'] = int(raw_registers[0].split(' ')[2])
registers['B'] = int(raw_registers[1].split(' ')[2])
registers['C'] = int(raw_registers[2].split(' ')[2])

program = list(map(int, raw_program_input.strip().split(' ')[1].split(',')))

def lookup_combo(combo):
    if combo >= 0 and combo <= 3:
        return int(combo)
    elif combo == 4:
        return registers['A']
    elif combo == 5:
        return registers['B']
    elif combo == 6:
        return registers['C']
    else:
        raise Exception("Invalid combo")

def adv(combo):
    registers['A'] = registers['A'] // pow(2, lookup_combo(combo))
def bxl(literal):
    registers['B'] = registers['B'] ^ literal
def bst(combo):
    registers['B'] = lookup_combo(combo) % 8
def jnz(literal):
    global ip
    if registers['A'] != 0:
        ip = literal-2
def bxc(_):
    registers['B'] = registers['B'] ^ registers['C']
def out(combo):
    output.append(str(lookup_combo(combo) % 8))
def bdv(combo):
    registers['B'] = registers['A'] // pow(2, lookup_combo(combo))
def cdv(combo):
    registers['C'] = registers['A'] // pow(2, lookup_combo(combo))

instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


while ip < len(program):
    instructions[program[ip]](program[ip+1])
    ip += 2

print(','.join(output))


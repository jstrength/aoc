import time
from pprint import pprint

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
        #print("LOOP")
        ip = literal-2
def bxc(_):
    registers['B'] = registers['B'] ^ registers['C']
def out(combo):
    output.append(lookup_combo(combo) % 8)
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

2,4, # B = A % 8
1,7, # B = B ^ 7
7,5, # C = A // pow(2, B)
1,7, # B = B ^ 7
4,6, # B = B ^ C
0,3, # A = A // pow(2, 3) (8)
5,5, # print B
3,0  # jump to beginning (0) if A != 0

#observations:
# remember this is a 3 bit computer
def algo(A):
    B = A & 7 # B = 0-7 this is actualling getting last 3 bits of A
    B = B ^ 7 # B = 7-B
    #C = pow(2, B) # C = 1-128, stepping by powers of 2
    #C = A // C
    C = A >> B
    B = B ^ 7 # reset B to original 0-7 on first line
    B = B ^ C
    A = A >> 3 # remove last 3 bits
    while A != 0:
        return [B % 8] + algo(A)
    return [B % 8]

#   print(program)
#   a = 35000000000000
#   a = 0
#   for i in range(1, len(program)):
#       tmp_a = a
#       for j in range(8):
#           a = tmp_a
#           j = j << (3*(len(program)-i))
#           a = a | j
#           ip = 0
#           output = []
#           registers['A'] = a
#           registers['B'] = int(raw_registers[1].split(' ')[2])
#           registers['C'] = int(raw_registers[2].split(' ')[2])
#   
#           while ip < len(program):
#               instructions[program[ip]](program[ip+1])
#               ip += 2
#   
#           print('output', output)
#           #print('\r', output, '\t', a, end='')
#           print(bin(a), '\t', a, '\t', program[len(program)-i], '\t', output[len(output)-i])
#           print(len(program), '\t', len(output))
#           #print(algo(a))
#   
#           if len(program) == len(output) and program[len(program)-i] == output[len(output)-i]:
#               print("FOUND")
#               print(a)
#               print(program)
#               print(output)
#               #a = a << 3
#               break
#       print()

#258386305814096 is too low



def find_a(a, i):
    tmp_a = a
    for j in range(8):
        print('INDEX', i, j)
        a = tmp_a
        j = j << (3*(len(program)-i))
        a = a | j

        print(a, i, j)
        output = algo(a)
        print(output)

        #print('\r', output, '\t', a, end='')
        print(bin(a), '\t', a, '\t', program[len(program)-i], '\t', output[len(output)-i])
        print(len(program), '\t', len(output))
        #print(algo(a))

        if len(program) == len(output) and program[len(program)-i] == output[len(output)-i]:
            print("FOUND")
            print(a)
            print(program)
            print(output)
            if i == len(program):
                print('DONE')
                return True
            if find_a(a, i+1):
                #a = a << 3
                return True
    print()
    return False

find_a(0, 1)




















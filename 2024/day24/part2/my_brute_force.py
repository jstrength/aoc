from itertools import combinations
from copy import deepcopy

bit_size = 5

raw_initial_state, raw_initial_gates = open("big_input.txt").read().split("\n\n")

initial_states = {x.split(': ')[0]: int(x.split(': ')[1]) for x in raw_initial_state.split('\n')}

initial_gates = {}
for initial_gate in raw_initial_gates.strip().split('\n'):
    inputs, gate = initial_gate.split(' -> ')
    initial_gates[tuple(inputs.split(' '))] = gate

def run(states, gates):
    while True:
        next_gates = {}
        for gate in gates:
            l, op, r = gate

            if not (l in states and r in states):
                next_gates[gate] = gates[gate]
                continue

            state = gates[gate]
            match op:
                case 'AND':
                    states[state] = states[l] & states[r]
                case 'OR':
                    states[state] = states[l] | states[r]
                case 'XOR':
                    states[state] = states[l] ^ states[r]

        if not next_gates:
            break
        if len(next_gates) == len(gates):
            break

        gates = next_gates

def get_variable(states, var):
    bits = []
    for i in range(bit_size):
        curr = f'{var}{i:02d}'
        if curr in states:
            bits.append(states[curr])
        else:
            break
    if bits:
        return int(''.join(map(str, reversed(bits))), 2)
    else:
        return 0

gates_keys = list(initial_gates.keys())
combos = list(combinations(gates_keys, 2))

swapped_wires = []

my_states = initial_states.copy()
my_gates = deepcopy(initial_gates)

for i in range(1, 45):
    bit_size = i

    my_states = initial_states.copy()
    my_gates = deepcopy(initial_gates)

    #print(a, b, end='\t')
    x = get_variable(my_states, 'x')
    y = get_variable(my_states, 'y')

    run(my_states, my_gates)
    bit_size += 1
    z = get_variable(my_states, 'z')
    bit_size -= 1

    print(x, y, z)

    if x+y == z:
        print('good', bit_size)
        continue


    print('bad', bit_size)

    for a,b in combos:
        my_gates = deepcopy(initial_gates)
        my_states = initial_states.copy()

        #print(a, b, end='\t')
        x = get_variable(my_states, 'x')
        y = get_variable(my_states, 'y')

        my_gates[a], my_gates[b] = my_gates[b], my_gates[a]

        run(my_states, my_gates)
        bit_size += 1
        z = get_variable(my_states, 'z')
        bit_size -= 1


        if x+y != z:
            my_gates[a], my_gates[b] = my_gates[b], my_gates[a]
        else:
            print('.', end='', flush=True)
            swapped_wires.append(my_gates[a])
            swapped_wires.append(my_gates[b])
            print('swapping', swapped_wires)
            print(bit_size)
            break

print(swapped_wires)
print(','.join(swapped_wires))


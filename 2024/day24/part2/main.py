from collections import defaultdict
from pprint import pprint

bit_size = 45

raw_initial_state, raw_initial_gates = open("big_input2.txt").read().split("\n\n")

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

            for state in gates[gate]:
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


circuit = {}

def check_half_adders(bit):
    x = f"x{bit:02d}"
    y = f"y{bit:02d}"
    #find the carry
    for gate in initial_gates:
        l, op, r = gate
        if l == x and r == y and op == 'XOR' or l == y and r == x and op == 'XOR':
            circuit[bit] = {'x':x, 'y':y, 'first_xor':(gate, initial_gates[gate])}
            break
    if bit == 0:
        return True
    if not circuit[bit]['first_xor']:
        print('no first xor')
        return False


    for gate in initial_gates:
        l, op, r = gate
        if l == circuit[bit]['first_xor'][1] and op == 'XOR':
            circuit[bit]['carry'] = r
            break
        if r == circuit[bit]['first_xor'][1] and op == 'XOR':
            circuit[bit]['carry'] = l
            break
    if 'carry' not in circuit[bit]:
        print('no carry')
        print(circuit[bit]['first_xor'])
        return False

    for gate in initial_gates:
        l, op, r = gate
        if l == circuit[bit]['first_xor'][1] and r == circuit[bit]['carry'] and op == 'XOR' or \
            r == circuit[bit]['first_xor'][1] and l == circuit[bit]['carry'] and op == 'XOR':
            circuit[bit]['second_xor'] = (gate, initial_gates[gate])
    if 'second_xor' not in circuit[bit]:
        print('no second xor')
        return False

    for gate in initial_gates:
        l, op, r = gate
        if l == circuit[bit]['first_xor'][1] and r == circuit[bit]['carry'] and op == 'AND' or \
            r == circuit[bit]['first_xor'][1] and l == circuit[bit]['carry'] and op == 'AND':
            circuit[bit]['first_and'] = (gate, initial_gates[gate])
    if 'first_and' not in circuit[bit]:
        print('no first and')
        return False

    for gate in initial_gates:
        l, op, r = gate
        if l == x and r == y and op == 'AND' or l == y and r == x and op == 'AND':
            circuit[bit]['second_and'] = (gate, initial_gates[gate])
    if 'second_and' not in circuit[bit]:
        print('no second and')
        return False

    for gate in initial_gates:
        l, op, r = gate
        if l == circuit[bit]['first_and'][1] and r == circuit[bit]['second_and'][1] and op == 'OR' or \
            r == circuit[bit]['first_and'][1] and l == circuit[bit]['second_and'][1] and op == 'OR':
            circuit[bit]['or'] = (gate, initial_gates[gate])
    if 'or' not in circuit[bit]:
        print('no or')
        return False

    return True

for bit in range(bit_size):
    check_half_adders(bit)

for bit in circuit:
    if bit != 0 and len(circuit[bit]) != 8:
        print('bad circuit')
        print(bit)
        pprint(circuit[bit])
#pprint(circuit)

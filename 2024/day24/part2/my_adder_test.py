raw_initial_state, raw_initial_gates = open("big_input.txt").read().split("\n\n")

bit_size = 2

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

y = get_variable(initial_states, 'y')
x = get_variable(initial_states, 'x')

run(initial_states, initial_gates)
bit_size += 1
z = get_variable(initial_states, 'z')

print(x, y, z)

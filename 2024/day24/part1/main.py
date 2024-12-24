from collections import defaultdict

raw_initial_state, raw_initial_gates = open("big_input.txt").read().split("\n\n")

states = {x.split(': ')[0]: int(x.split(': ')[1]) for x in raw_initial_state.split('\n')}

gates = defaultdict(list)
for initial_gate in raw_initial_gates.strip().split('\n'):
    inputs, gate = initial_gate.split(' -> ')
    gates[tuple(inputs.split(' '))].append(gate)

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

    gates = next_gates

bits = []
for i in range(len(states)):
    curr = f'z{i:02d}'
    if curr in states:
        bits.append(states[curr])
    else:
        break

print(int(''.join(map(str, reversed(bits))), 2))

from itertools import combinations
from copy import deepcopy
import signal
import sys

bit_size = 44

raw_initial_state, raw_initial_gates = open("big_input2.txt").read().split("\n\n")

initial_states = {x.split(': ')[0]: int(x.split(': ')[1]) for x in raw_initial_state.split('\n')}

initial_gates = {}
for initial_gate in raw_initial_gates.strip().split('\n'):
    inputs, gate = initial_gate.split(' -> ')
    initial_gates[tuple(inputs.split(' '))] = gate

sorted_gates = list(reversed(sorted(initial_gates.keys())))

def run(states, gates):
    my_sorted_gates = sorted_gates.copy()
    while True:
        removed = False
        for gate in my_sorted_gates:
            l, op, r = gate

            if not (l in states and r in states):
                continue

            removed = True
            my_sorted_gates.remove(gate)
            state = gates[gate]
            match op:
                case 'AND':
                    states[state] = states[l] & states[r]
                case 'OR':
                    states[state] = states[l] | states[r]
                case 'XOR':
                    states[state] = states[l] ^ states[r]

        if not my_sorted_gates or not removed:
            break


def is_bad_bit(test_bit, gates):
    my_initial_states = initial_states.copy()

    for i in range(bit_size):
        my_initial_states[f'x{i:02d}'] = 0
        my_initial_states[f'y{i:02d}'] = 0


    my_states = my_initial_states.copy()
    my_states[f'x{test_bit:02d}'] = 0
    my_states[f'y{test_bit:02d}'] = 0
    run(my_states, gates) 
    if f'z{test_bit:02d}' not in my_states or my_states[f'z{test_bit:02d}'] != 0:
        #print('bad bit found', test_bit)
        return True

    my_states = my_initial_states.copy()
    my_states[f'x{test_bit:02d}'] = 1
    my_states[f'y{test_bit:02d}'] = 1
    run(my_states, gates)
    if f'z{test_bit:02d}' not in my_states or my_states[f'z{test_bit:02d}'] != 0: #or \
        #f'z{(test_bit+1):02d}' not in my_states or my_states[f'z{(test_bit+1):02d}'] != 1:
        #print('bad bit found', test_bit)
        return True

    my_states = my_initial_states.copy()

    my_states[f'x{test_bit:02d}'] = 0
    my_states[f'y{test_bit:02d}'] = 1
    run(my_states, gates)
    if f'z{test_bit:02d}' not in my_states or my_states[f'z{test_bit:02d}'] != 1:
        #print('bad bit found', test_bit)
        return True

    my_states = my_initial_states.copy()
    my_states[f'x{test_bit:02d}'] = 1
    my_states[f'y{test_bit:02d}'] = 0
    run(my_states, gates)
    if f'z{test_bit:02d}' not in my_states or my_states[f'z{test_bit:02d}'] != 1:
        #print('bad bit found', test_bit)
        return True

    return False

def get_first_bad_bit_idx(gates, curr_bit_size):
    count = 0
    for test_bit in range(curr_bit_size+1):
        if is_bad_bit(test_bit, gates):
            return test_bit
    return count

def signal_handler(sig, frame):
    print()
    print(swapped_wires)
    sys.exit(0)

#signal.signal(signal.SIGINT, signal_handler)

prev_idx = 0
curr_bad_bit_idx = get_first_bad_bit_idx(initial_gates, bit_size)
print(curr_bad_bit_idx)
exit()

gates_keys = list(initial_gates.keys())
combos = list(combinations(gates_keys, 2))
swapped_wires = []

my_states = initial_states.copy()
my_gates = deepcopy(initial_gates)
print(len(combos))

while curr_bad_bit_idx != 0:
    print('|', end='', flush=True)
    #my_gates = deepcopy(initial_gates)
    #swapped_wires = []
    count = 0
    print()
    for a,b in combos:
        print(count, end='\r', flush=True)
        count += 1

        #print(a, b, end='\t')

        my_states = initial_states.copy()

        my_gates[a], my_gates[b] = my_gates[b], my_gates[a]

        run(my_states, my_gates)

        num_bad_bits = get_first_bad_bit_idx(my_gates, curr_bad_bit_idx)

        if num_bad_bits <= curr_bad_bit_idx:
            my_gates[a], my_gates[b] = my_gates[b], my_gates[a]
        elif num_bad_bits > curr_bad_bit_idx:
            print('.', end='', flush=True)
            print(num_bad_bits, end='')
            curr_bad_bit_idx = num_bad_bits
            swapped_wires.append(my_gates[a])
            swapped_wires.append(my_gates[b])
            break

print(swapped_wires)
print(','.join(swapped_wires))


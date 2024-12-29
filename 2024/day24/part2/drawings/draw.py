import schemdraw
from schemdraw import logic
from schemdraw.parsing import logicparse

raw_initial_state, raw_initial_gates = open("../input.txt").read().split("\n\n")

initial_states = {x.split(': ')[0]: int(x.split(': ')[1]) for x in raw_initial_state.split('\n')}

initial_gates = {}
for initial_gate in raw_initial_gates.strip().split('\n'):
    inputs, gate = initial_gate.split(' -> ')
    initial_gates[tuple(inputs.split(' '))] = gate

def create_and_gate(a, b, c):
    gate = logic.And()
    logic.Line().left(
def create_or_gate(a, b, c):
    return logic.Or(a, b)
def create_xor_gate(a, b, c):
    return logic.Xor(a, b)

with schemdraw.Drawing():
    for gate in initial_gates:
        l, op, r = gate
        match op:
            case 'AND':
                create_and_gate(l, r, initial_gates[gate])
            case 'OR':
                create_or_gate(l, r, initial_gates[gate])
            case 'XOR':
                create_xor_gate(l, r, initial_gates[gate])

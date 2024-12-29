#import mermaid as md
#from mermaid.graph import Graph
from pprint import pprint

raw_initial_state, raw_initial_gates = open("../big_input.txt").read().split("\n\n")

initial_states = {x.split(': ')[0]: int(x.split(': ')[1]) for x in raw_initial_state.split('\n')}

initial_gates = {}
for initial_gate in raw_initial_gates.strip().split('\n'):
    inputs, gate = initial_gate.split(' -> ')
    initial_gates[tuple(inputs.split(' '))] = gate


def create_graph(gates):
    id_counter = 0
    g = {}
    for gate in gates:
        id_counter += 1
        l, op, r = gate
        g[gates[gate]] = {'op': op, 'l': l, 'r': r}

    for gate in g:
        if not (g[gate]['l'][0] == 'x' or g[gate]['l'][0] == 'y'):
            g[gate]['l'] = g[g[gate]['l']]
            g[gate]['r'] = g[g[gate]['r']]

    while True:
        is_deleted = False
        for gate in g:
            if gate[0] != 'z':
                del g[gate]
                is_deleted = True
                break

        if not is_deleted:
            break
        
    return g

pprint(create_graph(initial_gates)['z03'])

#sequence = Graph('Sequence-diagram',raw_initial_gates)

#sequence = Graph('Sequence-diagram',"""
#stateDiagram-v2
#    [*] --> Still
#    Still --> [*]
#
#    Still --> Moving
#    Moving --> Still
#    Moving --> Crash
#    Crash --> [*]
#""")
#
#render = md.Mermaid(sequence)
#render # !! note this only works in the notebook that rendered the html.

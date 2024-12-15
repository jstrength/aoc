from pprint import pprint
from sympy import solve, core
from sympy.abc import a, b

#print(solve([a*94 + b*22 - 8400, a*34 + b*67 - 5400], a, b, dict=True))

lines = open("big_input.txt").read().splitlines()

big = 10000000000000
a_cost = 3
b_cost = 1
machines = []

for i in range(0, len(lines), 4):
    machine = {}
    machine["A"] = {i.split('+')[0]: int(i.split('+')[1]) for i in lines[i].split(": ")[1].split(", ")}    
    machine["B"] = {i.split('+')[0]: int(i.split('+')[1]) for i in lines[i+1].split(": ")[1].split(", ")}
    machine["P"] = {i.split('=')[0]: int(i.split('=')[1]) + big for i in lines[i+2].split(": ")[1].split(", ")}
    machines.append(machine)

tokens = 0
for machine in machines:
    #pprint(machine)
    curr_min = float('inf')

    results = solve([machine['A']['X']*a + machine['B']['X']*b - machine['P']['X'], \
        machine['A']['Y']*a + machine['B']['Y']*b - machine['P']['Y']], a, b, dict=True)
    if len(results) > 1:
        print("yes")
    for result in results:
        if isinstance(result[a], core.numbers.Integer) and \
            isinstance(result[b], core.numbers.Integer):
            curr_min = min(curr_min, a_cost*result[a] + b_cost*result[b])

    if curr_min != float('inf'):
        tokens += curr_min

print(tokens)

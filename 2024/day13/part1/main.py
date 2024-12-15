from pprint import pprint

lines = open("big_input.txt").read().splitlines()

a_cost = 3
b_cost = 1
machines = []

for i in range(0, len(lines), 4):
    machine = {}
    machine["A"] = {i.split('+')[0]: int(i.split('+')[1]) for i in lines[i].split(": ")[1].split(", ")}    
    machine["B"] = {i.split('+')[0]: int(i.split('+')[1]) for i in lines[i+1].split(": ")[1].split(", ")}
    machine["P"] = {i.split('=')[0]: int(i.split('=')[1]) for i in lines[i+2].split(": ")[1].split(", ")}
    machines.append(machine)

tokens = 0
for machine in machines:
    #pprint(machine)
    curr_min = float('inf')

    for a in range(1, 101):
        for b in range(1, 101):
            if machine['A']['X']*a + machine['B']['X']*b == machine['P']['X'] and \
                machine['A']['Y']*a + machine['B']['Y']*b == machine['P']['Y']:
                curr_min = min(curr_min, a_cost*a + b_cost*b)

    if curr_min != float('inf'):
        tokens += curr_min

print(tokens)

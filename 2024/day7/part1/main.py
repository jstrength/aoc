lines = open('big_input.txt').read().splitlines()

total_to_operands = {}

for line in lines:
    total, equation = line.split(':')
    total_to_operands[int(total)] = list(map(int, equation.split()))

def calculate(total, operands):
    if total == 0:
        return True
    if not operands:
        return False
    if len(operands) == 1:
        return calculate(total-operands[0], [])

    curr = operands[0]+operands[1]
    if calculate(total, [curr] + operands[2:]):
        return True

    curr = operands[0]*operands[1]
    if calculate(total, [curr] + operands[2:]):
        return True

    return False

sum_total = 0
for k, v in total_to_operands.items():
    if calculate(k, v):
        sum_total += k

print(sum_total)

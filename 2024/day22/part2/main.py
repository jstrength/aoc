lines = open("big_input.txt").read().splitlines()

initial_secret_numbers = [int(number) for number in lines]

def mix(secret_number, other_number):
    return secret_number ^ other_number

def prune(secret_number):
    return secret_number % 16777216

def calculate_new_secret_number(current_secret_number):
    step1 = prune(mix(current_secret_number, (current_secret_number * 64)))
    step2 = prune(mix(step1, int(step1 / 32)))
    return prune(mix(step2, step2 * 2048))

#secret_number = 123
#changes_lookup = {}
#changes = []
#seen = set()
#for _ in range(9):
#    previous_secret_number = secret_number
#    secret_number = calculate_new_secret_number(secret_number)
#    new_change = int(str(secret_number)[-1])
#    prev_change = int(str(previous_secret_number)[-1])
#    changes.append(new_change - prev_change)
#    if len(changes) > 3:
#        seq = tuple(changes[-4:])
#        if seq in seen:
#            continue
#        seen.add(seq)
#        if seq in changes_lookup:
#            changes_lookup[seq] += new_change
#        else:
#            changes_lookup[seq] = new_change
#
#print(changes)
#print(changes[1:])
#print()
#print(changes_lookup)
#print()
#exit()

changes_lookup = {}
for secret_number in initial_secret_numbers:
    changes = []
    seen = set()
    for _ in range(2000):
        previous_secret_number = secret_number
        secret_number = calculate_new_secret_number(secret_number)
        new_change = int(str(secret_number)[-1])
        prev_change = int(str(previous_secret_number)[-1])
        changes.append(new_change - prev_change)
        if len(changes) > 3:
            seq = tuple(changes[-4:])
            if seq in seen:
                continue
            seen.add(seq)
            if seq in changes_lookup:
                changes_lookup[seq] += new_change
            else:
                changes_lookup[seq] = new_change

max_seq = [float('-Inf'),()]
for k, v in changes_lookup.items():
    if v > max_seq[0]:
        max_seq = [v, k]

print(max_seq)

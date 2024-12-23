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

total = 0
for secret_number in initial_secret_numbers:
    for _ in range(2000):
        secret_number = calculate_new_secret_number(secret_number)
    total += secret_number
print(total)

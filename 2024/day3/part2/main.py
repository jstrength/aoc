import re

input = open("big_input.txt").read()
#print(input)
fixed_input = ""

enabled = True
for i in range(len(input)):
    if enabled:
        if input[i:i+7] == "don't()":
            enabled = False
    else:
        if input[i:i+4] == "do()":
            enabled = True
    if enabled:
        fixed_input += input[i]

#print(fixed_input)

matches = re.findall(r"mul\((?P<left>[0-9]{1,3}),(?P<right>[0-9]{1,3})\)", fixed_input)

#print(matches)

result = 0
for match in matches:
    #print(match)
    result += int(match[0]) * int(match[1])

print(result)



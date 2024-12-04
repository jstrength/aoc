import re

input = open("big_input.txt").read()
#print(input)

matches = re.findall(r"mul\((?P<left>[0-9]{1,3}),(?P<right>[0-9]{1,3})\)", input)

#print(matches)

result = 0
for match in matches:
    #print(match)
    result += int(match[0]) * int(match[1])

print(result)



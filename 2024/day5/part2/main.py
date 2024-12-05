from collections import defaultdict

lines = open("big_input.txt").readlines()

pages = []
updates = []

is_pages = True
for line in lines:
    line = line.strip()
    if line == '':
        is_pages = False
        continue

    if is_pages:
        pages.append(line)
    else:
        updates.append(line.split(","))


pages_lookup = defaultdict(list)
for page in pages:
    k,v = page.split("|")
    pages_lookup[k].append(v)

bad_updates = []

def is_bad_update(update):
    is_bad = False
    for i in range(len(update)):
        for n in pages_lookup[update[i]]:
            for j in range(i):
                if n == update[j]:
                    is_bad = True
                    tmp = update[j]
                    update[j] = update[i]
                    update[i] = tmp
    if is_bad:
        return update

for update in updates:
    if is_bad_update(update): 
        while is_bad_update(update):
            continue
        bad_updates.append(update)

#print("pages")
#print(pages)
#print("pages_lookup")
#print(pages_lookup)
#print("updates")
#print(updates)
#print("bad_updates")
#print(bad_updates)


middle_sum = 0
for update in bad_updates:
    middle_sum += int(update[len(update)//2])

print(middle_sum)

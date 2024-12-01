from collections import Counter

input = open("input.txt")

nums1 = []
nums2 = []
for line in input:
    num1, num2 = line.split()
    nums1.append(int(num1))
    nums2.append(int(num2))

freqs = Counter(nums2)
total = 0

for n in nums1:
    total += n*freqs[n]

print(total)

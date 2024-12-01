input = open("input.txt")

nums1 = []
nums2 = []
for line in input:
    num1, num2 = line.split()
    nums1.append(int(num1))
    nums2.append(int(num2))

nums1.sort()
nums2.sort()

total = 0

for i in range(len(nums1)):
    total += abs(nums1[i] - nums2[i])

print(total)

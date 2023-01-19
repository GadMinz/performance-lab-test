import sys

with open(sys.argv[1]) as numsFile:
    numsData = numsFile.read().split('\n')
nums = list(map(int, numsData))
median = sorted(nums)[len(nums) // 2]
result = 0

for v in nums:
    result += abs(v - median)

print(result)

import sys
file = open(sys.argv[1], 'r')
nums = []
for line in file:
    nums.append(int(line))
nums = sorted(nums)
minstps = 0
median = nums[len(nums)//2]
for i in range(len(nums)):
    minstps += abs(nums[i] - median)
print(minstps)
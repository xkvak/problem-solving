import sys

sys_input = sys.stdin.readline
n = int(sys_input())
nums = list(int(sys_input()) for _ in range(n))
memo = {}

for i in range(n):
    for j in range(n):
        memo[nums[i] + nums[j]] = True

max_value = 0
for i in range(n):
    for j in range(n):
        total = abs(nums[i] - nums[j])
        if total in memo:
            max_value = max(max_value, nums[i])

print(max_value)

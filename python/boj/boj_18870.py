import sys

sys_input = sys.stdin.readline
n = int(sys_input().rstrip())
nums = list(map(int, sys_input().split()))
sorted_nums = sorted(list(set(nums)))


def find_left_idx(target: int, nums: list):
    start = 0
    end = len(nums)

    while start < end:
        mid = int((start + end) / 2)
        if nums[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start


idx_dict = {}
result = []
for n in nums:
    if n not in idx_dict:
        idx_dict[n] = find_left_idx(n, sorted_nums)
    result.append(idx_dict[n])

print(*result)

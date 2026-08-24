import sys

sys_input = sys.stdin.readline
n, m = map(int, sys_input().split())
a = sorted([int(sys_input()) for _ in range(n)])
left, right = 0, 0
result = 3000000000

while right < n:
    diff = a[right] - a[left]
    if diff == m:
        result = diff
        break

    if diff < m:
        right += 1
    else:
        result = min(result, diff)
        left += 1

print(result)

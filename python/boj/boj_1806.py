import sys

sys_input = sys.stdin.readline
n, s = map(int, sys_input().split())
a = list(map(int, sys_input().split()))

left, right = 0, 0
total = a[left]
result = 0x7FFFFFFF

while True:
    if total < s:
        right += 1
        if right == n:
            break
        total += a[right]
    else:
        result = min(result, right - left + 1)
        total -= a[left]
        left += 1

if result == 0x7FFFFFFF:
    result = 0
print(result)

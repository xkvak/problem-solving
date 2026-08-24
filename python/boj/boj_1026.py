import sys

sys_input = sys.stdin.readline
n = int(sys_input().rstrip())
a = sorted(list(map(int, sys_input().split())))
b = sorted(list(map(int, sys_input().split())), reverse=True)

result = 0
for i in range(n):
    result += a[i] * b[i]
print(result)

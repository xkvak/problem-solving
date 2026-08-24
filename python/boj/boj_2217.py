import sys

sys_input = sys.stdin.readline
n = int(sys_input())
ropes = sorted([int(sys_input().rstrip()) for _ in range(n)])
result = 0
for i in range(0, len(ropes)):
    result = max(result, ropes[i] * (len(ropes) - i))

print(result)

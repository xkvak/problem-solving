import sys

sys_input = sys.stdin.readline
n = int(sys_input())
request_list = sorted([list(map(int, sys_input().split())) for _ in range(n)])
cnt = 1
min_end = 2147483647

for start, end in request_list:
    if min_end <= start:
        cnt += 1
        min_end = end
    else:
        min_end = min(min_end, end)

print(cnt)

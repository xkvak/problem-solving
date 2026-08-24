import sys

sys_input = sys.stdin.readline
n, k = map(int, sys_input().split())
coins = list(int(sys_input().rstrip()) for _ in range(n))
idx = n - 1
cnt = 0

while k != 0:
    while coins[idx] <= k:
        k -= coins[idx]
        cnt += 1
    idx -= 1
print(cnt)

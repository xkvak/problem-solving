"""boj 2293. 동전 1"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, k, arr):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in arr:
        for price in range(1, k + 1):
            prev = price - coin
            if prev < 0:
                continue
            dp[price] += dp[prev]
    return dp[k]


def main():
    n, k = map(int, sys_input().split())
    arr = [int(sys_input()) for _ in range(n)]
    print(solve(n, k, arr))


if __name__ == "__main__":
    main()

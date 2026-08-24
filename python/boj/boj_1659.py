"""백준 1659. 팰린드롬 만들기"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, arr):
    ans = 0
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if arr[left] == arr[right]:
                dp[left][right] = dp[left + 1][right - 1]
            else:
                dp[left][right] = min(dp[left + 1][right], dp[left][right - 1]) + 1

    ans = dp[0][n - 1]
    return ans


def main():
    n = int(sys_input())
    arr = list(map(int, sys_input().split()))
    print(solve(n, arr))


if __name__ == "__main__":
    main()

"""백준 9461. 파도반 수열"""

import sys


def sys_input() -> str:
    return sys.stdin.readline()


def main():
    dp = [0] * 100
    dp[0], dp[1], dp[2] = 1, 1, 1
    for i in range(3, 100):
        dp[i] = dp[i - 2] + dp[i - 3]

    k = int(sys_input())
    for _ in range(k):
        n = int(sys_input())
        print(dp[n - 1])


if __name__ == "__main__":
    main()

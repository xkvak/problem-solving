"""백준 10942. 팰린드롬?"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, arr, m, questions):
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = 1

    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if arr[start] == arr[end] and dp[start + 1][end - 1]:
                dp[start][end] = 1

    return dp


def main():
    n = int(sys_input())
    arr = list(map(int, sys_input().split()))
    m = int(sys_input())
    questions = list(tuple(map(int, sys_input().split())) for _ in range(m))
    ans = solve(n, arr, m, questions)
    for a, b in questions:
        print(1 if ans[a - 1][b - 1] else 0)


if __name__ == "__main__":
    main()

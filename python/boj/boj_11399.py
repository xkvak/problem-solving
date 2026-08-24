"""백준 11399. ATM"""

import sys


def sys_stdin() -> str:
    return sys.stdin.readline().rstrip()


def solve(arr):
    arr.sort()
    tmp = 0
    ans = 0
    for num in arr:
        tmp = tmp + num
        ans += tmp
    return ans


def main():
    n = int(sys_stdin())
    arr = list(map(int, sys_stdin().split()))
    print(solve(arr))


if __name__ == "__main__":
    main()

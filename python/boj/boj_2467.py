"""백준 2467. 용액"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, arr):
    ans = [0] * 2
    min_val = 10**10
    left, right = 0, n - 1
    while left < right:
        diff = arr[left] + arr[right]
        if abs(diff) <= min_val:
            min_val = abs(diff)
            ans[0], ans[1] = arr[left], arr[right]

        if 0 < diff:
            right -= 1
        else:
            left += 1

    return ans


def main():
    n = int(sys_input())
    arr = list(map(int, sys_input().split()))
    print(*solve(n, arr))


if __name__ == "__main__":
    main()

"""백준 2138. 전구와 스위치"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


INF = 10**9


def solve(n, arr, t):
    def press(arr, i):
        for j in (i - 1, i, i + 1):
            if 0 <= j < len(arr):
                arr[j] ^= 1

    def simulate(press_first_switch):
        a = arr[:]
        cnt = 0
        if press_first_switch:
            press(a, 0)
            cnt += 1

        for i in range(1, n):
            if a[i - 1] != t[i - 1]:
                press(a, i)
                cnt += 1

        if a[-1] != t[-1]:
            cnt += 1

        return cnt if a == t else INF

    ans = min(simulate(True), simulate(False))
    return ans if ans != INF else -1


def main():
    n = int(sys_input())
    arr = list(map(int, sys_input()))
    t = list(map(int, sys_input()))
    print(solve(n, arr, t))


if __name__ == "__main__":
    main()

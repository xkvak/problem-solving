"""백준 11003. 최솟값 찾기"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().strip()


INF = pow(10, 10)


def solve(n, l, a):
    result = []
    dq = deque()
    for i in range(n):
        while dq and dq[0] < i - l + 1:
            dq.popleft()

        while dq and a[dq[-1]] > a[i]:
            dq.pop()

        dq.append(i)
        result.append(a[dq[0]])
    return result


def search_min_val(a):
    min_val = INF
    min_idx = -1
    for idx, val in enumerate(a):
        if val < min_val:
            min_val = val
            min_idx = idx
    return (min_val, min_idx)


def main():
    n, l = map(int, sys_input().split())
    a = list(map(int, sys_input().split()))
    print(*solve(n, l, a))


if __name__ == "__main__":
    main()

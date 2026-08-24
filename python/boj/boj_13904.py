"""백준 13940. 과제"""

import heapq
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, assignments: dict):
    ans = 0
    arr = []
    keys = sorted(assignments.keys())
    for curr in keys:
        for val in assignments[curr]:
            heapq.heappush(arr, val)

        while curr < len(arr):
            heapq.heappop(arr)

    for score in arr:
        ans += score

    return ans


def main():
    n = int(sys_input())
    a = {}
    for _ in range(n):
        d, w = map(int, sys_input().split())
        a.setdefault(d, []).append(w)
    print(solve(n, a))


if __name__ == "__main__":
    main()

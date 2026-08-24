"""백준 13334. 철로"""

import heapq
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(arr: list, d: int) -> int:
    ans = 0
    h = []
    for start, end in arr:
        heapq.heappush(h, start)
        while h:
            tmp = heapq.heappop(h)
            if end - d <= tmp:
                heapq.heappush(h, tmp)
                break
        ans = max(ans, len(h))

    return ans


def main():
    n = int(sys_input())
    arr = []
    for _ in range(n):
        a, b = map(int, sys_input().split())
        arr.append((min(a, b), max(a, b)))
    arr.sort(key=lambda x: x[1])
    d = int(sys_input())
    print(solve(arr, d))


if __name__ == "__main__":
    main()

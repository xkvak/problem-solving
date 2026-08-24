"""백준 8980.택배"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, c, adj):
    load = [0] * (n + 1)
    result = 0
    for start, end, box in adj:
        possible = box
        for i in range(start, end):
            possible = min(possible, c - load[i])

        for i in range(start, end):
            load[i] += possible

        result += possible
    return result


def main():
    n, c = map(int, sys_input().split())
    m = int(sys_input())
    adj = []
    for _ in range(m):
        a, b, box = map(int, sys_input().split())
        adj.append((a, b, box))
    adj.sort(key=lambda x: (x[1], x[0]))
    print(solve(n, c, adj))


if __name__ == "__main__":
    main()

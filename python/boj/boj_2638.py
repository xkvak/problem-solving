"""백준 2638. 치즈"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, m, adj):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    time = 0

    while True:
        time += 1
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        dq = deque([(0, 0)])
        while dq:
            cy, cx = dq.popleft()
            for dy, dx in directions:
                my, mx = cy + dy, cx + dx
                if my < 0 or mx < 0 or n <= my or m <= mx:
                    continue

                if adj[my][mx] == 0 and visited[my][mx] == 0:
                    dq.append((my, mx))
                    visited[my][mx] = 1
                if adj[my][mx] == 1:
                    visited[my][mx] += 1

        cheese_cnt = 0
        for y in range(n):
            for x in range(m):
                if 1 < visited[y][x]:
                    adj[y][x] = 0
                if adj[y][x] == 1:
                    cheese_cnt += 1

        if cheese_cnt == 0:
            return time


def main():
    n, m = map(int, sys_input().split())
    adj = [list(map(int, sys_input().split())) for _ in range(n)]
    print(solve(n, m, adj))


if __name__ == "__main__":
    main()

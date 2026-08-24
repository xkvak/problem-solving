"""code for 11780. 플로이드2"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, adj: list, nxt: list) -> tuple[list, list]:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if adj[i][k] + adj[k][j] < adj[i][j]:
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                    nxt[i][j] = nxt[i][k]
    return adj, nxt


def main():
    inf = 0x3F3F3F3F
    n = int(sys_input())
    m = int(sys_input())
    adj = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    nxt = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, sys_input().split())
        adj[a][b] = min(adj[a][b], c)
        nxt[a][b] = b

    adj, nxt = solve(n, adj, nxt)

    for i in range(1, n + 1):
        result = []
        for j in range(1, n + 1):
            if adj[i][j] == inf:
                result.append(0)
            else:
                result.append(adj[i][j])
        print(*result)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] == 0 or adj[i][j] == inf:
                print(0)
                continue

            path = deque()
            st = i
            while st != j:
                path.append(st)
                st = nxt[st][j]
            path.append(j)

            result = []
            result.append(len(path))
            while path:
                result.append(path.popleft())
            print(*result)


if __name__ == "__main__":
    main()

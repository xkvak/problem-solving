"""백준 17073.나무 위의 빗물"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().strip()


def solve(n, w, adj):
    ans = 0
    cnt = 0

    is_visited = [False] * (n + 1)
    is_visited[1] = True
    dq = deque([(1, w)])

    while dq:
        curr_idx, curr_water = dq.popleft()
        if curr_idx == 1:
            child_cnt = len(adj[curr_idx])
        else:
            child_cnt = len(adj[curr_idx]) - 1

        if child_cnt == 0:
            cnt += 1
            ans += curr_water
            continue

        nxt_water = curr_water / child_cnt
        for nxt in adj[curr_idx]:
            if is_visited[nxt]:
                continue

            dq.append((nxt, nxt_water))
            is_visited[nxt] = True

    return ans / cnt


def main():
    n, w = map(int, sys_input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys_input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(solve(n, w, adj))


if __name__ == "__main__":
    main()

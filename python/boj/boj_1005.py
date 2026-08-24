"""백준 1005. ACM Craft"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, times, adj, indegree_cnt, w):
    result = [0] * (n + 1)
    dq = deque()
    for i in range(1, n + 1):
        if indegree_cnt[i] == 0:
            dq.append(i)
            result[i] = times[i - 1]

    while dq:
        curr = dq.popleft()
        for nxt in adj[curr]:
            indegree_cnt[nxt] -= 1
            result[nxt] = max(result[nxt], result[curr] + times[nxt - 1])
            if indegree_cnt[nxt] == 0:
                dq.append(nxt)
    return result[w]


def main():
    t = int(sys_input())
    for _ in range(t):
        n, k = map(int, sys_input().split())
        times = list(map(int, sys_input().split()))
        adj = [[] for _ in range(n + 1)]
        indegree_cnt = [0 for _ in range(n + 1)]
        for _ in range(k):
            a, b = map(int, sys_input().split())
            adj[a].append(b)
            indegree_cnt[b] += 1
        w = int(sys_input())
        print(solve(n, times, adj, indegree_cnt, w))


if __name__ == "__main__":
    main()

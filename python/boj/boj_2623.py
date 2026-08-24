"""백준 2623. 음악프로그램"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, m, arr) -> list:
    adj = [[] for _ in range(n + 1)]
    indegree_cnt = [0] * (n + 1)

    for row in arr:
        for i in range(2, len(row)):
            adj[row[i - 1]].append(row[i])
            indegree_cnt[row[i]] += 1

    dq = deque()
    for i in range(1, len(indegree_cnt)):
        if indegree_cnt[i] == 0:
            dq.append(i)

    ans = []
    while dq:
        curr = dq.popleft()
        ans.append(curr)
        for nxt in adj[curr]:
            indegree_cnt[nxt] -= 1
            if indegree_cnt[nxt] == 0:
                dq.append(nxt)

    return ans


def main():
    n, m = map(int, sys_input().split())
    arr = list(list(map(int, sys_input().split())) for _ in range(m))
    ans = solve(n, m, arr)
    if len(ans) == n:
        print(*ans, sep="\n")
    else:
        print(0)


if __name__ == "__main__":
    main()

"""백준 14567. 선수과목"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, d, indegree_cnt):
    result = [-1] * (n + 1)
    dq = deque()

    for i in range(1, n + 1):
        if indegree_cnt[i] == 0:
            dq.append(i)
            result[i] = 1

    while dq:
        curr = dq.popleft()
        for nxt in d[curr]:
            indegree_cnt[nxt] -= 1
            if indegree_cnt[nxt] == 0:
                dq.append(nxt)
                result[nxt] = result[curr] + 1
    return result


def main():
    n, m = map(int, sys_input().split())
    d = [[] * (n + 1) for _ in range(n + 1)]
    indegree_cnt = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, sys_input().split())
        d[a].append(b)
        indegree_cnt[b] += 1

    print(*solve(n, d, indegree_cnt)[1:])


if __name__ == "__main__":
    main()

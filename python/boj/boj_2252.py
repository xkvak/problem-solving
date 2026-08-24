from collections import deque
import sys

sys_input = sys.stdin.readline
n, m = map(int, sys_input().split())
a = [[] for _ in range(n + 1)]
indegree_cnt = [0 for _ in range(n + 1)]
indegree_cnt[0] = -1
for _ in range(m):
    p1, p2 = map(int, sys_input().split())
    a[p1].append(p2)
    indegree_cnt[p2] += 1

q = deque()
for idx, val in enumerate(indegree_cnt):
    if val == 0:
        q.append(idx)

result = []
while q:
    curr = q.popleft()
    result.append(curr)
    for nxt in a[curr]:
        indegree_cnt[nxt] -= 1
        if indegree_cnt[nxt] == 0:
            q.append(nxt)

print(*result)

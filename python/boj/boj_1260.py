from collections import deque
import sys

sys_input = sys.stdin.readline
n, m, v = map(int, sys_input().split())
graph = list([] for _ in range(n + 1))
for _ in range(m):
    a, b = map(int, sys_input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()


def bfs(graph: list, v):
    q = deque([v])
    visited = [v]
    while q:
        for nxt in graph[q.popleft()]:
            if not nxt in visited:
                visited.append(nxt)
                q.append(nxt)
    return visited


visited = [v]


def dfs(graph: list, v):
    for next in graph[v]:
        if not next in visited:
            visited.append(next)
            dfs(graph, next)


dfs(graph, v)

print(*visited)
print(*bfs(graph, v))

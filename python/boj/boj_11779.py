"""11779. 최소비용 구하기 2"""

import heapq
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


INF = 0x3F3F3F3F


def solve(n, adj, start, end):
    min_distances = [INF] * (n + 1)
    min_distances[start] = 0
    heap = [(0, start)]
    visited = [0] * (n + 1)
    while heap:
        curr_val, curr_idx = heapq.heappop(heap)
        if min_distances[curr_idx] < curr_val:
            continue

        for nxt_idx, nxt_val in adj[curr_idx]:
            nxt_val += curr_val
            if nxt_val < min_distances[nxt_idx]:
                heapq.heappush(heap, (nxt_val, nxt_idx))
                min_distances[nxt_idx] = nxt_val
                visited[nxt_idx] = curr_idx
    seq = []
    while end != start:
        seq.append(end)
        end = visited[end]
    seq.append(start)
    return min_distances, list(reversed(seq))


def main():
    n = int(sys_input())
    m = int(sys_input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys_input().split())
        adj[a].append((b, c))

    start, end = map(int, sys_input().split())
    distance, vistied = solve(n, adj, start, end)
    print(distance[end])
    print(len(vistied))
    print(*vistied)


if __name__ == "__main__":
    main()

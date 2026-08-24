"""code for 1753. 최단경로"""

import heapq
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


INF = 0x3F3F3F3F


def solve(v, k, adj) -> list:
    heap = []
    heapq.heappush(heap, (0, k))
    distance = [INF] * (v + 1)
    distance[k] = 0

    while heap:
        curr_dist, curr = heapq.heappop(heap)
        if distance[curr] < curr_dist:
            continue

        for nxt_idx, nxt_value in adj[curr]:
            new_dist = curr_dist + nxt_value
            if new_dist < distance[nxt_idx]:
                heapq.heappush(heap, (new_dist, nxt_idx))
                distance[nxt_idx] = min(distance[nxt_idx], new_dist)
    return distance


def main():
    v, e = map(int, sys_input().split())
    k = int(sys_input())
    adj = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b, c = map(int, sys_input().split())
        adj[a].append((b, c))

    result = solve(v, k, adj)[1:]
    for i in range(v):
        print("INF" if result[i] == INF else result[i])


if __name__ == "__main__":
    main()

import bisect
import heapq
import sys

sys_input = sys.stdin.readline
n, k = map(int, sys_input().split())
crystal = [tuple(map(int, sys_input().split())) for _ in range(n)]
bags = [int(sys_input()) for _ in range(k)]
crystal.sort(key=lambda x: x[0])
bags.sort()

heap = []
result = 0
idx = 0

for bag in bags:
    while idx < n and crystal[idx][0] <= bag:
        heapq.heappush(heap, -crystal[idx][1])
        idx += 1

    if heap:
        result += -heapq.heappop(heap)

print(result)

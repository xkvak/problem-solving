import heapq
import sys

sys_input = sys.stdin.readline
t = int(sys_input())
for _ in range(t):
    k = int(sys_input())
    min_queue = []
    max_queue = []
    visited = [False] * 1000001

    for i in range(k):
        operation, value = sys_input().split()
        value = int(value)

        if operation == "I":
            heapq.heappush(min_queue, (value, i))
            heapq.heappush(max_queue, (-value, i))
            visited[i] = True
        elif operation == "D":
            if value == 1:
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)
            else:
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[min_queue[0][1]] = False
                    heapq.heappop(min_queue)

    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)

    if not min_queue:
        print("EMPTY")
    else:
        print(-max_queue[0][0], min_queue[0][0])

from collections import Counter
import heapq
import sys

sys_input = sys.stdin.readline
n = int(sys_input())
a = [int(sys_input()) for _ in range(n)]
heap = []
count = {}

for num in a:
    count[num] = count.get(num, 0) + 1
    if num == 0:
        if heap:
            min_num = heapq.heappop(heap)
            if 0 < count.get(-min_num, 0):
                print(-min_num)
                count[-min_num] = count.get(-min_num, 0) - 1
            else:
                print(min_num)
                count[min_num] = count.get(min_num, 0) - 1
        else:
            print(0)
    else:
        heapq.heappush(heap, abs(num))

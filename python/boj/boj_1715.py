import heapq
import sys

sys_input = sys.stdin.readline
n = int(sys_input())
q = sorted([int(sys_input()) for _ in range(n)])
result = 0

while 1 < len(q):
    new_deck = heapq.heappop(q) + heapq.heappop(q)
    result += new_deck
    heapq.heappush(q, new_deck)

if n == 1:
    print(0)
else:
    print(result)

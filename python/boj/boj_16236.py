"""백준 16236. 아기 상어"""

from collections import deque
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


# 현재 위치에서 갈 수 있는 모든 곳에 대한 거리를 구한다.
# 가장 가까운 위치로 이동히고 이동한 거리만큼 asn에 더하고, size도 1만큼 커진다.
# 이 과정을 갈 수 있는 곳이 없을때까지 반복한다.
def solve(n: int, adj: list) -> int:
    ans = 0
    size = 2
    inf = 10**10
    curr = None
    for i, row in enumerate(adj):
        for j, v in enumerate(row):
            if int(v) == 9:
                curr = (i, j)
                adj[i][j] = 0

    visited = [[False] * n for _ in range(n)]
    eat_cnt = 0
    while True:
        min_dist = inf
        nxt = None
        dist = count_distance(curr, adj, n, size)
        for i, row in enumerate(dist):
            for j, v in enumerate(row):
                v = int(v) - 1
                if size <= adj[i][j] or visited[i][j] or v == -1 or adj[i][j] == 0:
                    continue

                if v < min_dist:
                    min_dist = v
                    nxt = (i, j)

        if nxt is None:
            break

        curr = nxt
        ans += min_dist
        eat_cnt += 1
        visited[curr[0]][curr[1]] = True

        if eat_cnt == size:
            size += 1
            eat_cnt = 0

    return ans


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def count_distance(curr: tuple[int, int], adj, n, size):
    q = deque([curr])
    visited = [[0] * n for _ in range(n)]
    visited[curr[0]][curr[1]] = 1

    while q:
        curr_y, curr_x = q.popleft()
        for dy, dx in DIRECTIONS:
            moved_y, moved_x = dy + curr_y, dx + curr_x
            if moved_y < 0 or moved_x < 0 or n <= moved_y or n <= moved_x:
                continue
            if visited[moved_y][moved_x] != 0:
                continue
            if size < int(adj[moved_y][moved_x]):
                continue

            visited[moved_y][moved_x] = visited[curr_y][curr_x] + 1
            q.append((moved_y, moved_x))

    return visited


def main():
    n = int(sys_input())
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j, v in enumerate(sys_input().split()):
            adj[i][j] = int(v)

    print(solve(n, adj))


if __name__ == "__main__":
    main()

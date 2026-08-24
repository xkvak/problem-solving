"""programmers pccp 4. 수레 움직이기"""

from collections import deque


def solution(maze):
    n, m = len(maze), len(maze[0])
    red_start = red_target = blue_start = blue_target = None
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == 1:
                red_start = (y, x)
            elif val == 2:
                blue_start = (y, x)
            elif val == 3:
                red_target = (y, x)
            elif val == 4:
                blue_target = (y, x)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    red_visited = set([red_start])
    blue_visited = set([blue_start])
    dq = deque([(red_start, blue_start, red_visited, blue_visited, 0)])
    while dq:
        red_pos, blue_pos, red_visited, blue_visited, turn = dq.popleft()
        red_y, red_x = red_pos
        blue_y, blue_x = blue_pos
        if red_pos == red_target and blue_pos == blue_target:
            return turn

        red_nxt_postions, blue_nxt_positions = [], []
        for dy, dx in directions:
            if red_pos == red_target:
                red_nxt_postions = [red_pos]
                break

            nxt_red_pos = (red_y + dy, red_x + dx)
            nxt_red_y, nxt_red_x = nxt_red_pos

            if nxt_red_y < 0 or nxt_red_x < 0 or n <= nxt_red_y or m <= nxt_red_x:
                continue
            if nxt_red_pos in red_visited:
                continue
            if maze[nxt_red_y][nxt_red_x] == 5:
                continue
            red_nxt_postions.append(nxt_red_pos)

        for dy, dx in directions:
            if blue_pos == blue_target:
                blue_nxt_positions = [blue_pos]
                break

            nxt_blue_pos = (blue_y + dy, blue_x + dx)
            nxt_blue_y, nxt_blue_x = nxt_blue_pos

            if nxt_blue_y < 0 or nxt_blue_x < 0 or n <= nxt_blue_y or m <= nxt_blue_x:
                continue
            if nxt_blue_pos in blue_visited:
                continue
            if maze[nxt_blue_y][nxt_blue_x] == 5:
                continue
            blue_nxt_positions.append(nxt_blue_pos)

        for nxt_red_pos in red_nxt_postions:
            for nxt_blue_pos in blue_nxt_positions:
                if nxt_red_pos == nxt_blue_pos:
                    continue
                if nxt_red_pos == blue_pos and nxt_blue_pos == red_pos:
                    continue

                new_red_visited, new_blue_visited = (
                    red_visited.copy(),
                    blue_visited.copy(),
                )
                new_red_visited.add(nxt_red_pos)
                new_blue_visited.add(nxt_blue_pos)
                dq.append(
                    (
                        nxt_red_pos,
                        nxt_blue_pos,
                        new_red_visited,
                        new_blue_visited,
                        turn + 1,
                    )
                )

    return 0


if __name__ == "__main__":
    print(solution([[1, 5], [2, 5], [4, 5], [3, 5]]))

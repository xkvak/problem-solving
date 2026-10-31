class Solution:
    """leetcode 3665. Twisted Mirror Path Count"""

    def uniquePaths(self, grid: list[list[int]]) -> int:
        mod = pow(10, 9) + 7
        n, m = len(grid), len(grid[0])
        r = [[0] * m for _ in range(n)]
        d = [[0] * m for _ in range(n)]
        r[0][0] = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    to_right, to_down = d[i][j], r[i][j]
                else:
                    to_right = to_down = (r[i][j] + d[i][j]) % mod

                if j < m - 1:
                    r[i][j + 1] = (r[i][j + 1] + to_right) % mod
                if i < n - 1:
                    d[i + 1][j] = (d[i + 1][j] + to_down) % mod

        return (r[n - 1][m - 1] + d[n - 1][m - 1]) % mod


if __name__ == "__main__":
    print(Solution().uniquePaths([[0, 1, 1], [1, 1, 0]]))

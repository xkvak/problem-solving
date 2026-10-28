class Solution:
    """leetcode 3882. Minimum XOR Path in a Grid"""

    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[set() for _ in range(m)] for _ in range(n)]
        dp[0][0] = {grid[0][0]}

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                prev = set()
                if i > 0:
                    prev |= dp[i - 1][j]
                if j > 0:
                    prev |= dp[i][j - 1]
                dp[i][j] = {num ^ grid[i][j] for num in prev}

        return min(dp[n - 1][m - 1])


if __name__ == "__main__":
    print(Solution().minCost([[2, 7, 5], [1, 2, 3]]))

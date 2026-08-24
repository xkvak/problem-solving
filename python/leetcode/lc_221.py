class Solution:
    """leetcode 221. Maximal Square"""

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ans = 0
        n = len(matrix)
        dp = [list(map(int, row)) for row in matrix]
        for y, row in enumerate(dp):
            for x, val in enumerate(row):
                if y <= 0 or x <= 0:
                    ans = max(ans, dp[y][x])
                    continue
                if dp[y][x] == 0:
                    continue

                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
                ans = max(ans, dp[y][x])

        return ans**2


if __name__ == "__main__":
    print(Solution().maximalSquare([["0", "0"], ["0", "0"]]))

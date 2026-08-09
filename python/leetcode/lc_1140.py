from functools import cache


class Solution:
    """leetcode 1140. Stone Game II"""

    def stoneGameII(self, piles: list[int]) -> int:
        @cache
        def dp(i, m):
            if i >= n:
                return 0

            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                oppnent_best = dp(i + x, max(x, m))
                my_score = suffix_sum[i] - oppnent_best
                best = max(best, my_score)

            return best

        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        return dp(0, 1)


if __name__ == "__main__":
    print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))

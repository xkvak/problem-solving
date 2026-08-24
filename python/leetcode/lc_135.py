# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 135. Candy"""

    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        dp = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                dp[i] = dp[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                dp[i - 1] = max(dp[i - 1], dp[i] + 1)

        return sum(dp)


if __name__ == "__main__":
    print(Solution().candy([1, 6, 10, 8, 7, 3, 2]))

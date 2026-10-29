class Solution:
    """leetcode 2144. Minimum Cost of Buying Candies With Discount"""

    def minmumCost(self, cost: list[int]) -> int:
        return sum(cost) - sum(sorted(cost, reverse=True)[2::3])


if __name__ == "__main__":
    print(Solution().minmumCost([6, 5, 7, 9, 2, 2]))

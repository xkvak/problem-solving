# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 122. Best Time to Buy and Sell Stock 2"""

    def maxProfit_first(self, prices: list[int]) -> int:
        ans = 0
        n = len(prices)
        buy = 0

        if sorted(prices, reverse=True) == prices:
            return 0

        while buy < n:
            for i in range(buy, n - 1):
                if prices[i] > prices[i + 1]:
                    buy = i + 1
                    break

            sell = buy + 1
            for i in range(sell, n - 1):
                if prices[i] > prices[i + 1]:
                    sell = i
                    break

            if n <= buy or n <= sell:
                break

            profit = prices[sell] - prices[buy]
            if 0 < profit:
                ans += profit
            buy = sell

        return ans

    def maxProfit_second(self, prices: list[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans


if __name__ == "__main__":
    print(Solution().maxProfit_second([7, 6, 4, 3, 1]))

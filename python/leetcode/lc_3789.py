class Solution:
    """leetcode 3789. Minimum Cost to Acquire Required Items"""

    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        ans = 0
        if cost1 + cost2 <= costBoth:
            ans = cost1 * need1 + cost2 * need2
        else:
            if need1 < need2:
                ans = costBoth * need1
                ans += min(cost2, costBoth) * (need2 - need1)
            else:
                ans = costBoth * need2
                ans += min(cost1, costBoth) * (need1 - need2)

        return ans


if __name__ == "__main__":
    print(Solution().minimumCost(cost1=5, cost2=4, costBoth=15, need1=0, need2=0))

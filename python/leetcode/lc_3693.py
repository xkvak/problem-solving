class Solution:
    """leetcode 3693. Climbing Stairs II"""

    def climbStairs(self, n: int, costs: list[int]) -> int:
        d = [0] * (n + 1)
        for j in range(1, n + 1):
            val = costs[j - 1] + pow(j - (j - 1), 2) + d[j - 1]
            if 1 < j:
                val = min(val, costs[j - 1] + pow(j - (j - 2), 2) + d[j - 2])
            if 2 < j:
                val = min(val, costs[j - 1] + pow(j - (j - 3), 2) + d[j - 3])
            d[j] = val
        return d[n]


if __name__ == "__main__":
    print(Solution().climbStairs(n=4, costs=[5, 1, 6, 2]))

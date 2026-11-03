class Solution:
    """leetcode 3736. Minimum Moves to Equal Array Elements III"""

    def minMoves(self, nums: list[int]) -> int:
        return max(nums) * len(nums) - sum(nums)


if __name__ == "__main__":
    print(Solution().minMoves([4, 4, 5]))

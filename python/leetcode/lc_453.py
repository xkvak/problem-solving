class Solution:
    """leetcode 453. Minimum Moves to Equal Array Elements"""

    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3, 4]))

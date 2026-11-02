class Solution:
    """leetcode 462. Minimum Moves to Equal Array Elements II"""

    def minMoves2(self, nums: list[int]) -> int:
        mid = sorted(nums)[len(nums) // 2]
        ans = 0
        for n in nums:
            ans += abs(mid - n)
        return ans


if __name__ == "__main__":
    print(Solution().minMoves2([3, 0, 6, 2, 4, 7, 0, 0]))

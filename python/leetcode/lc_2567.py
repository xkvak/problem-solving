# @lc app=leetcode id=2567 lang=python3


# @lc code=start
class Solution:
    """leetcode 2567. Minimum Score by Changing Two Elements"""

    def minimizeSum(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        return min(nums[n - 1] - nums[2], nums[n - 3] - nums[0], nums[n - 2] - nums[1])


# @lc code=end


if __name__ == "__main__":
    print(Solution().minimizeSum(nums=[1, 4, 7, 8, 5]))

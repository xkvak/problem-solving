# @lc app=leetcode id=3041 lang=python3


# @lc code=start
class Solution:
    """leetcode 3041. Maximize Consecutive Elements in an Array After Modification"""

    def maxSelectedElements(self, nums: list[int]) -> int:
        n = len(nums)
        dp = {}
        nums.sort()
        for n in nums:
            dp[n + 1] = dp.get(n, 0) + 1
            dp[n] = dp.get(n - 1, 0) + 1

        return max(dp.values())


# @lc code=end


if __name__ == "__main__":
    print(Solution().maxSelectedElements(nums=[2, 1, 5, 1, 1]))

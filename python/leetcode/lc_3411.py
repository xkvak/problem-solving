# @lc app=leetcode id=3411 lang=python3

# @lc code=start
import math


class Solution:
    """leetcode 3411. Maximum Subarray With Equal Products"""

    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if math.prod(nums[i:j]) == math.gcd(*nums[i:j]) * math.lcm(*nums[i:j]):
                    ans = max(ans, j - i)
        return ans


# @lc code=end


if __name__ == "__main__":
    print(Solution().maxLength(nums=[2, 3, 4, 5, 6]))

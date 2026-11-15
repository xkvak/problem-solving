# @lc app=leetcode id=1524 lang=python3


# @lc code=start
class Solution:
    """leetcode 1524. Number of Sub-arrays With Odd Sum"""

    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        pre_odd, pre_even = 0, 1
        presum = 0
        for num in arr:
            presum += num
            if presum % 2:
                pre_odd += 1
                ans += pre_even
            else:
                pre_even += 1
                ans += pre_odd

        return ans % (10**9 + 7)


# @lc code=end


if __name__ == "__main__":
    print(Solution().numOfSubarrays(arr=[1, 3, 5]))

# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 918.  Maximum Sum Circular Subarray"""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums)
        curr_min, curr_max = nums[0], nums[0]
        min_sum, max_sum = nums[0], nums[0]

        for num in nums[1:]:
            curr_min = min(num, curr_min + num)
            curr_max = max(num, curr_max + num)
            min_sum = min(min_sum, curr_min)
            max_sum = max(max_sum, curr_max)

        if total == min_sum:
            return max_sum
        return max(max_sum, total - min_sum)


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular(list([-3, -2, -3])))

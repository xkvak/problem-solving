# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 238. Product of Array Except Self"""

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        total = 1
        for i in range(n):
            num = nums[i]
            total *= num
            prefix[i] = total

        total = 1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            total *= num
            suffix[i] = total

        for i in range(n):
            multi = prefix[i - 1] if 0 < i else 1
            if i < n - 1:
                multi *= suffix[i + 1]
            ans.append(multi)
        return ans


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))

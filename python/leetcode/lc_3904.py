class Solution:
    """leetcode 3904. Smallest Stable Index II"""

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_nums = []
        min_val = nums[-1]
        for num in nums[::-1]:
            min_val = min(min_val, num)
            min_nums.append(min_val)
        min_nums = min_nums[::-1]

        max_val = nums[0]
        for i in range(n):
            max_val = max(nums[i], max_val)
            if max_val - min_nums[i] <= k:
                return i

        return -1


if __name__ == "__main__":
    print(Solution().firstStableIndex([2, 0, 2], 2))

# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 80. Remove Duplicates from Sorted Array 2"""

    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        idx = 0
        left, right = 0, 0
        while right < n:
            while nums[left] == nums[right] and right < n - 1:
                right += 1

            distance = right - left if right - left < 2 else 2
            for _ in range(distance):
                nums[idx] = nums[left]
                idx += 1

            left = right
            right += 1

        distance = right - left if right - left < 2 else 2
        for _ in range(distance):
            nums[idx] = nums[left]
            idx += 1

        nums = nums[:idx]
        if nums[-3:] == [nums[-1]] * 3:
            nums = nums[:-1]
        return len(nums)


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1]))

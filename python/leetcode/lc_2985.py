from collections import defaultdict, deque
from re import I


class Solution:
    """leetcode 2958. Length of Longest Subarray With at Most K Frequency"""

    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        cnt = defaultdict(int)
        ans = 0

        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    print(Solution().maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))

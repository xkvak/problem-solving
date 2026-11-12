class Solution:
    """leetcode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray"""

    def method_name(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                cnt[i][0] = cnt[i - 1][0] + 1
            elif nums[i - 1] > nums[i]:
                cnt[i][1] = cnt[i - 1][1] + 1

        return max(map(max, cnt))


if __name__ == "__main__":
    print(Solution().method_name([1, 4, 3, 3, 2]))

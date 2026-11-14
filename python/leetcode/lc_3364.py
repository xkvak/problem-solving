class Solution:
    """leetcode 3364. Minimum Positive Sum Subarray"""

    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 10**9
        for length in range(l, r + 1):
            for end in range(length, n + 1):
                s = prefix[end] - prefix[end - length]
                if s > 0:
                    ans = min(ans, s)

        return ans if ans != 10**9 else -1


if __name__ == "__main__":
    print(Solution().minimumSumSubarray([3, -2, 1, 4], 2, 3))

from functools import cache


class Solution:
    """ leetcode 486. Predict the Winner """

    def predictTheWinner(self, nums: list[int]) -> bool:
        @cache
        def dp(l, r) -> int:
            if l == r:
                return nums[l]
            return max(nums[l] - dp(l + 1, r), nums[r] - dp(l, r - 1))
            
        return dp(0, len(nums) - 1) >= 0


if __name__ == "__main__":
    print(Solution().predictTheWinner([1,5,233,7]))

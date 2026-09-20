from collections import defaultdict


class Solution:
    """leetcode 2615. Sum of Distances"""

    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        posisions = defaultdict(list)
        for i, num in enumerate(nums):
            posisions[num].append(i)

        ans = [0] * n
        for group in posisions.values():
            total = sum(group)
            size = len(group)
            left = 0
            for rank, curr in enumerate(group):
                right = total - left - curr
                ans[curr] = (rank * curr - left) + (right - (size - 1 - rank) * curr)
                left += curr

        return ans


if __name__ == "__main__":
    print(Solution().distance([1, 3, 1, 1, 2]))

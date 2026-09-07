from collections import defaultdict


class Solution:
    """leetcode 3740. Minimum Distance Between Three Equal Elements I"""

    # (0, 1, 5) => 1 + 4 + 4 = 9
    def minimumDistance(self, nums: list[int]) -> int:
        group = defaultdict(list)
        for idx, num in enumerate(nums):
            group[num].append(idx)

        ans = 0x7FFFFFFF
        for indices in group.values():
            for i in range(2, len(indices)):
                total = (
                    abs(indices[i] - indices[i - 1])
                    + abs(indices[i - 1] - indices[i - 2])
                    + abs(indices[i - 2] - indices[i])
                )
                ans = min(ans, total)

        return -1 if ans == 0x7FFFFFFF else ans


if __name__ == "__main__":
    print(Solution().minimumDistance([5, 5, 5, 2, 5]))

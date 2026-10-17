class Solution:
    """leetcode 3551. Minimum Swaps to Sort by Digit Sum"""

    def minSwap(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(sorted_nums)}
        visited = [False] * n
        cnt = 0
        for i in range(n):
            if visited[i]:
                continue
            cnt += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]

        return n - cnt


if __name__ == "__main__":
    print(Solution().minSwap([18, 43, 34, 16]))

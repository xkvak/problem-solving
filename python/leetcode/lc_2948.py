class Solution:
    """leetcode 2948. Make Lexicographically Smallest Array by Swapping Elements"""

    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        ans = [0] * n
        indexed = sorted(enumerate(nums), key=lambda x: x[1])

        start = 0
        for end in range(1, n + 1):
            if end == n or indexed[end][1] - indexed[end - 1][1] > limit:
                chunk = indexed[start:end]
                for i, (_, v) in zip(sorted(idx for idx, _ in chunk), chunk):
                    ans[i] = v
                start = end

        return ans


if __name__ == "__main__":
    print(Solution().lexicographicallySmallestArray(nums=[1, 7, 6, 18, 2, 1], limit=3))

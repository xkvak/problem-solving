class Solution:
    """leetcode 1385. Find the Distance Value Between Two Arrays"""

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d) -> int:
        margin = 1101
        prefix = [0] * 2202
        for num in arr2:
            prefix[num + margin] = 1
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        ans = 0
        for num in arr1:
            if not prefix[num + margin + d] - prefix[num + margin - d - 1]:
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))

class Solution:
    """leetcode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum"""

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = 10**9

        prefix = [INF] * n
        left, total, best = 0, 0, INF
        for right in range(n):
            total += arr[right]
            while target < total:
                total -= arr[left]
                left += 1
            if target == total:
                best = min(best, right - left + 1)
            prefix[right] = best

        suffix = [INF] * n
        right, total, best = n - 1, 0, INF
        for left in range(n - 1, -1, -1):
            total += arr[left]
            while target < total:
                total -= arr[right]
                right -= 1
            if target == total:
                best = min(best, right - left + 1)
            suffix[left] = best

        ans = INF
        for i in range(n - 1):
            ans = min(ans, prefix[i] + suffix[i + 1])

        return ans if ans < INF else -1


if __name__ == "__main__":
    print(Solution().minSumOfLengths(arr=[7, 3, 4, 7], target=7))

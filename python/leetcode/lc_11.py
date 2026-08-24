# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 11. Container With Most Water"""

    def max_area(self, height: list[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r]) * (r - l)
            ans = max(ans, h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == "__main__":
    print(Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

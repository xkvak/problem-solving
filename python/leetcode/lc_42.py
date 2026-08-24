# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 42. Trapping Rain Water"""

    def trap(self, args) -> int:
        ans = 0
        n = len(args)
        wall = args[0]
        max_val, max_idx = 0, 0
        for i, num in enumerate(args):
            if max_val <= num:
                max_idx = i
                max_val = num

        for i in range(max_idx + 1):
            h = args[i]
            if h < wall:
                ans += wall - h
            else:
                wall = h

        wall = args[-1]
        for i in range(n - 1, max_idx, -1):
            h = args[i]
            if h < wall:
                ans += wall - h
            else:
                wall = h

        return ans


if __name__ == "__main__":
    print(Solution().trap([4, 2, 0, 3, 2, 5]))

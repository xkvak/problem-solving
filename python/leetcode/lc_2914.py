# @lc app=leetcode id=2914 lang=python3


# @lc code=start
class Solution:
    """leetcode 2914. Minimum Number of Changes to Make Binary String Beautiful"""

    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(0, n, 2):
            ans += min(s[i : i + 2].count("0"), s[i : i + 2].count("1"))
        return ans


# @lc code=end


if __name__ == "__main__":
    print(Solution().minChanges(s="1001"))

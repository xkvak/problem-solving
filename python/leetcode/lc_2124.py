# @lc app=leetcode id=2124 lang=python3


# @lc code=start
class Solution:
    """leetcode 2124. Check if All A's Appears Before All B's"""

    def checkString(self, s: str) -> bool:
        n = len(s)
        lt = 0
        while lt < n and s[lt] == "a":
            lt += 1
        rt = lt
        while rt < n and s[rt] == "b":
            rt += 1

        return rt == n


# @lc code=end


if __name__ == "__main__":
    print(Solution().checkString(s="aaabbb"))

class Solution:
    """leetcode 921. Minimum Add to Make Parentheses Valid"""

    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = 0
        for ch in s:
            if ch == "(":
                stack += 1
            else:
                if stack == 0:
                    ans += 1
                else:
                    stack -= 1

        ans += stack
        return ans


if __name__ == "__main__":
    print(Solution().minAddToMakeValid("())"))

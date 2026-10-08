class Solution:
    """leetcode 1021. Remove Outermost Parentheses"""

    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        nest = 0
        for ch in s:
            if ch == "(":
                nest += 1
                if nest > 1:
                    ans.append(ch)
            else:
                nest -= 1
                if nest > 0:
                    ans.append(ch)

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().removeOuterParentheses("(()())(())"))

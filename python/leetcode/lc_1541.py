class Solution:
    """leetcode 1541. Minimum Insertions to Balance a Parentheses String"""

    def minInsertions(self, s: str) -> int:
        ans, need = 0, 0
        for ch in s:
            if ch == "(":
                if need % 2:
                    ans += 1
                    need -= 1
                need += 2
            else:
                if need == 0:
                    ans += 1
                    need = 2
                need -= 1
        return ans + need


if __name__ == "__main__":
    print(Solution().minInsertions("(()))(()))()())))"))

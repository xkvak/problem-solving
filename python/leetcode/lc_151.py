# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 151. Reverse Words in a String"""

    def reverseWords(self, s: str) -> str:
        ans = ""
        s = " " + s.strip()
        n = len(s) - 1
        prev = n + 1
        i = n - 1
        while -1 < i:
            if s[i] == " ":
                cnt = 0
                while s[i - cnt] == " ":
                    cnt += 1
                ans += s[i + 1 : prev] + " "
                i -= cnt
                prev = i + 1
            i -= 1

        return ans.strip()


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))

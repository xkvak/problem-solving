# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 67. Add Binary"""

    def addBinart(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ans = []

        while 0 <= i or 0 <= j or carry:
            total = carry

            if 0 <= i:
                total += int(a[i])
                i -= 1
            if 0 <= j:
                total += int(b[j])
                j -= 1

            ans.append(str(total % 2))
            carry = total // 2

        return "".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().addBinart("1010", "1011"))

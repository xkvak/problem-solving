# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 201. Bitwise AND of Numbers Range"""

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(416, 436))

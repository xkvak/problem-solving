# @lc app=leetcode id=2243 lang=python3


# @lc code=start
class Solution:
    """leetcode 2243. Calculate Digit Sum of a String"""

    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[i : i + k] for i in range(0, len(s), k)]
            s = "".join([str(sum(map(int, group))) for group in groups])
        return s


# @lc code=end


if __name__ == "__main__":
    print(Solution().digitSum(s="11111222223", k=3))

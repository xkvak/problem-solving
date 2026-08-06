from math import prod


class Solution:
    """ leetcode 3345. Smallest Divisible Digit Product I """

    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            ans = 1
            curr = n
            while curr:
                ans *= curr % 10
                curr //= 10
            if ans % t == 0: return n
            n += 1


if __name__ == "__main__":
    print(Solution().smallestNumber(15, 3))

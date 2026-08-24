# pylint: disable=too-few-public-methods
from collections import deque
import math


class Solution:
    """leetcode 150. Evaluate Reversee Polish Notation"""

    def evalRPN(self, tokens: list[str]) -> int:
        stack: deque[int] = deque()
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "-":
                    stack.append(n2 - n1)
                elif t == "*":
                    stack.append(n2 * n1)
                elif t == "/":
                    stack.append(math.trunc(n2 / n1))
            else:
                stack.append(int(t))

        return stack.pop()


if __name__ == "__main__":
    print(Solution().evalRPN(tokens=["3", "11", "5", "+", "-"]))

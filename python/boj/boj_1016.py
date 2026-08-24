"""백준 1016. 제곱 ㄴㄴ 수"""

import math
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(start: int, end: int):
    is_sqrt = [False] * (end - start + 1)
    i = 2

    while i * i <= end:
        square = i * i
        first = (math.ceil(start / square)) * square
        for j in range(first, end + 1, square):
            is_sqrt[j - start] = True
        i += 1
    return is_sqrt.count(False)


def main():
    a, b = map(int, sys_input().split())
    print(solve(a, b))


if __name__ == "__main__":
    main()

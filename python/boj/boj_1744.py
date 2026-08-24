"""백준 1744. 수 묶기"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(arr: list[int]):
    ans = 0
    positive, negative = [], []
    for num in arr:
        if num == 1:
            ans += 1
        elif 0 < num:
            positive.append(num)
        else:
            negative.append(num)

    positive.sort(reverse=True)
    for i in range(1, len(positive), 2):
        a, b = positive[i - 1], positive[i]
        ans += a * b
    if len(positive) % 2 == 1:
        ans += positive[-1]

    negative.sort()
    for i in range(1, len(negative), 2):
        a, b = negative[i - 1], negative[i]
        ans += a * b
    if len(negative) % 2 == 1:
        ans += negative[-1]

    return ans


def main():
    n = int(sys_input())
    arr = list(int(sys_input()) for _ in range(n))
    print(solve(arr))


if __name__ == "__main__":
    main()

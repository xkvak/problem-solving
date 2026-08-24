"""백준 1062. 가르침"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def combinations(alpahbet, depth):
    result = []

    def dfs(start, curr):
        if len(curr) == depth:
            result.append(curr)
            return

        for i in range(start, len(alpahbet)):
            dfs(i + 1, curr + alpahbet[i])

    dfs(0, "")
    return result


def solve(n, k, arr):
    if k < 5:
        return 0
    if k == 26:
        return n

    ans = 0
    base = ["a", "n", "t", "i", "c"]
    alphabet = [i for i in [chr(i) for i in range(97, 123)] if i not in base]

    combs = combinations(alphabet, k - 5)
    words = [set(i for i in word if i not in base) for word in arr]

    for c in combs:
        learned = set(c)
        count = 0

        for word in words:
            if word.issubset(learned):
                count += 1
        ans = max(ans, count)

    return ans


def main():
    n, k = map(int, sys_input().split())
    arr = [sys_input() for _ in range(n)]
    print(solve(n, k, arr))


if __name__ == "__main__":
    main()

"""백준 16987. 계란으로 계란치기"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, arr):

    def dfs(curr) -> int:
        if curr >= n:
            return sum(1 for num in arr if num[0] <= 0)

        if arr[curr][0] <= 0:
            return dfs(curr + 1)

        hit = False
        ans = 0
        for nxt in range(n):
            if nxt == curr:
                continue
            if arr[nxt][0] <= 0:
                continue

            hit = True
            arr[curr][0] -= arr[nxt][1]
            arr[nxt][0] -= arr[curr][1]
            ans = max(ans, dfs(curr + 1))
            arr[curr][0] += arr[nxt][1]
            arr[nxt][0] += arr[curr][1]

        if not hit:
            ans = max(ans, dfs(curr + 1))

        return ans

    return dfs(0)


def main():
    n = int(sys_input())
    arr = [list(map(int, sys_input().split())) for _ in range(n)]
    print(solve(n, arr))


if __name__ == "__main__":
    main()

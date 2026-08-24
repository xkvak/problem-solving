"""백준 1613. 역사"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, k, arr, s, t):

    def dfs(arr, curr, visited) -> set:
        result = set(arr[curr])
        for n in arr[curr]:
            if visited[n]:
                continue

            visited[n] = True
            result.update(dfs(arr, n, visited))
        return result

    adj = [[] for _ in range(n + 1)]
    for a, b in arr:
        adj[a].append(b)

    for i in range(1, n + 1):
        adj[i] = dfs(adj, i, [[] for _ in range(n + 1)])

    ans = []
    for a, b in t:
        if b in adj[a]:
            ans.append(-1)
        elif a in adj[b]:
            ans.append(1)
        else:
            ans.append(0)
    return ans


def main():
    n, k = map(int, sys_input().split())
    arr = list(tuple(map(int, sys_input().split())) for _ in range(k))
    s = int(sys_input())
    t = list(tuple(map(int, sys_input().split())) for _ in range(s))
    print(*solve(n, k, arr, s, t), sep="\n")


if __name__ == "__main__":
    main()

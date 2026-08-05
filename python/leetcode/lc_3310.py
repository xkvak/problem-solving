class Solution:
    """ leetcode 3310. Remove Methods From Project """

    def reaminingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        visited = set([k])
        for a, b in invocations:
            adj[a].append(b)

        stack = [k]
        while stack:
            curr = stack.pop()
            for nxt in adj[curr]:
                if nxt not in visited:
                    stack.append(nxt)
                    visited.add(nxt)

        for a, b in invocations:
            if b in visited and a not in visited:
                return list(range(n))

        return [i for i in range(n) if not i in visited]


if __name__ == "__main__":
    print(Solution().reaminingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]))

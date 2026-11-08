class Solution:
    """leetcode 3558. Number of Ways to Assign Edge Weights I"""

    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        def dfs(curr):
            for nxt in d[curr]:
                if visited[nxt] == 0:
                    visited[nxt] = visited[curr] + 1
                    dfs(nxt)

        n = len(edges)
        d = [[] for _ in range(n + 2)]
        visited = [0] * (n + 2)
        visited[1] = 1
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        dfs(1)
        k = max(visited) - 2
        return pow(2, k, 10**9 + 7)


if __name__ == "__main__":
    print(Solution().assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))

# pylint: disable=too-few-public-methods
from collections import defaultdict


class Solution:
    """leetcode 399. Evaluate Division"""

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(curr, target, visited: set, total: float) -> float:
            if curr == target:
                return total

            visited.add(curr)
            for nxt, val in graph[curr]:
                if nxt in visited:
                    continue

                result = dfs(nxt, target, visited, total * val)
                if result != -1.0:
                    return result

            return -1.0

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set(), 1.0))
        return ans


if __name__ == "__main__":
    print(
        Solution().calcEquation(
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )

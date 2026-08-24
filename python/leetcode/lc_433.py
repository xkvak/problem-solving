# pylint: disable=too-few-public-methods
from collections import defaultdict, deque


class Solution:
    """leetcode 433. Minimum Genetic Mutation"""

    """
    목표: bank 유전자 간에 연결 그래프를 생성한다.
    1. bank에 들어 있는 유전자를 순환한다.
    2. 유전자의 모든 철자를 하나씩 바꿔보며 bank에 들어 있는 유전자일 경우 연결한다.
    3. 연결 그래프에서 start -> end 까지 거리를 bfs를 통해 구한다.
    """

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        candidates = ["A", "C", "G", "T"]
        graph: dict[str, set[str]] = {}
        bank.append(startGene)
        for gene in bank:
            graph.setdefault(gene, set())

        for gene in bank:
            for idx in range(len(gene)):
                for candiate in candidates:
                    new_gene = gene[:idx] + candiate + gene[idx + 1 :]
                    if new_gene in graph:
                        graph[new_gene].add(gene)
                        graph[gene].add(new_gene)

        def dfs(curr: str, visited: set, cnt: int):
            if curr == endGene:
                return cnt

            ans = 9999
            for nxt in graph[curr]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                ans = min(ans, dfs(nxt, visited, cnt + 1))
                visited.remove(nxt)
            return ans

        ans = dfs(startGene, set(), 0)
        return -1 if ans == 9999 else ans


if __name__ == "__main__":
    print(
        Solution().minMutation(
            startGene="AAAACCCC",
            endGene="CCCCCCCC",
            bank=[
                "AAAACCCA",
                "AAACCCCA",
                "AACCCCCA",
                "AACCCCCC",
                "ACCCCCCC",
                "CCCCCCCC",
                "AAACCCCC",
                "AACCCCCC",
            ],
        )
    )

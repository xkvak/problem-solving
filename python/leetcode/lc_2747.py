class Solution:
    """leetcode 2747. Count Zero Request Servers"""

    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        logs.sort(key=lambda log: log[1])
        cnt = [0] * (n + 1)
        activate = 0
        ans = [0] * len(queries)
        l = r = 0

        for q, i in sorted((q, i) for i, q in enumerate(queries)):
            while r < len(logs) and logs[r][1] <= q:
                s = logs[r][0]
                if cnt[s] == 0:
                    activate += 1
                cnt[s] += 1
                r += 1

            while l < r and logs[l][1] < q - x:
                s = logs[l][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    activate -= 1
                l += 1
            ans[i] = n - activate

        return ans


if __name__ == "__main__":
    print(
        Solution().countServers(
            n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11]
        )
    )

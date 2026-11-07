import heapq


class Solution:
    """leetcode 1882. Process Tasks Using Servers"""

    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free, busy = [], []
        for server_idx, server_weight in enumerate(servers):
            heapq.heappush(free, (server_weight, server_idx))

        ans = []
        curr = 0
        for j, duration in enumerate(tasks):
            curr = max(curr, j)
            if not free:
                curr = max(j, busy[0][0])

            while busy and busy[0][0] <= curr:
                _, idx = heapq.heappop(busy)
                heapq.heappush(free, (servers[idx], idx))

            server_weight, server_idx = heapq.heappop(free)
            ans.append(server_idx)
            heapq.heappush(busy, (curr + duration, server_idx))

        return ans


if __name__ == "__main__":
    print(Solution().assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]))

# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 134. Gas Station"""

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        ans = 0
        n = len(gas)
        remaining_gas = []
        diff = 0
        for i in range(n):
            diff += gas[i] - cost[i]
            if diff < 0:
                diff = 0
                ans = i + 1
            remaining_gas.append(gas[i] - cost[i])
        return ans if 0 <= sum(remaining_gas) else -1


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))

# @lc app=leetcode id=3331 lang=python3


# @lc code=start
class Solution:
    """leetcode 3331. Find Subtree Sizes After Changes"""

    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        def dfs(x):
            idx = ord(s[x]) - 97
            tmp = last[idx]
            last[idx] = x
            for y in d[x]:
                dfs(y)
            last[idx] = tmp

            new_parent = tmp if tmp != -1 else parent[x]
            if new_parent != -1:
                ans[new_parent] += ans[x]

        n = len(parent)
        d = [list() for _ in range(n)]
        last = [-1] * 26
        ans = [1] * n
        for i in range(1, n):
            d[parent[i]].append(i)

        dfs(0)
        return ans


# @lc code=end


if __name__ == "__main__":
    print(Solution().findSubtreeSizes(parent=[-1, 0, 0, 1, 1, 1], s="abaabc"))

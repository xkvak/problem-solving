from python.leetcode.lc_106 import TreeNode


class Solution:
    """leetcode 2265. Count Nodes Equal to Average of Subtree"""

    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(curr) -> tuple[int, int]:
            nonlocal ans
            if not curr:
                return (0, 0)

            left_sum, left_cnt = dfs(curr.left)
            right_sum, right_cnt = dfs(curr.right)
            total_sum = left_sum + right_sum + curr.val
            total_cnt = left_cnt + right_cnt + 1

            if curr.val == total_sum // total_cnt:
                ans += 1
            return (total_sum, total_cnt)

        dfs(root)
        return ans


if __name__ == "__main__":
    print(Solution().averageOfSubtree(TreeNode()))

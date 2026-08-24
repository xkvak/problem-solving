# pylint: disable=too-few-public-methods

from collections import deque
from turtle import right
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal"""

    # def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    #     postorder_stack = deque(postorder)

    #     def build(self, arr: list[int]) -> TreeNode:
    #         root_val = postorder_stack.pop()
    #         root_idx = arr.index(root_val)
    #         left = arr[:root_idx]
    #         right = arr[root_idx + 1:]

    #         result = TreeNode(root_val)
    #         if right:
    #             result.right = build(self, right)
    #         if left:
    #             result.left = build(self, left)

    #         return result

    #     ans = build(self, inorder)
    #     return ans

    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        postorder_idx = len(postorder) - 1

        def build(left, right) -> Optional[TreeNode]:
            nonlocal postorder_idx

            if left > right:
                return None

            root_val = postorder[postorder_idx]
            postorder_idx -= 1

            root = TreeNode(root_val)
            root_idx = inorder_idx[root_val]

            root.right = build(root_idx + 1, right)
            root.left = build(left, root_idx - 1)
            return root

        ans = build(0, len(inorder) - 1)
        return ans


if __name__ == "__main__":
    print(Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))

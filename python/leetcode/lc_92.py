# pylint: disable=too-few-public-methods
from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """leetcode 92. Reverse Linked List 2"""

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        start = ListNode(0, head)
        prev = start
        for _ in range(left - 1):
            prev = prev.next

        curr: ListNode = prev.next
        for _ in range(right - left):
            tmp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = tmp

        return start.next


if __name__ == "__main__":
    pass
    # print(Solution().reverseBetween(test_args))

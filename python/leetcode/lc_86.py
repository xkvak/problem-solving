# pylint: disable=too-few-public-methods
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_array(cls, arr):
        if not arr:
            return None

        head = cls(arr[0])
        current = head

        for value in arr[1:]:
            current.next = cls(value)
            current = current.next

        return head


class Solution:
    """leetcode 86. Partition List"""

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(), ListNode()
        before_head, after_head = before, after

        while head:
            if head.val < x:
                before.next = ListNode(head.val)
                before = before.next
            else:
                after.next = ListNode(head.val)
                after = after.next
            head = head.next

        before.next = after_head.next
        return before_head.next


if __name__ == "__main__":
    print(Solution().partition(head=ListNode.from_array([1, 4, 3, 2, 5, 2]), x=3))

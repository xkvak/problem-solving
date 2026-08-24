# pylint: disable=too-few-public-methods

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """leetcode 82. Remove Duplicates from Sorted List2"""

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        cnt = {}
        while head.next:
            cnt[head.val] = cnt.get(head.val, 0) + 1
            head = head.next
        cnt[head.val] = cnt.get(head.val, 0) + 1

        ans = ListNode(0, None)
        copy = ans
        for k in cnt.keys():
            v = cnt[k]
            if 1 < v:
                continue
            ans.next = ListNode(k, None)
            ans = ans.next

        return copy.next


if __name__ == "__main__":
    print(Solution().deleteDuplicates(test_args))

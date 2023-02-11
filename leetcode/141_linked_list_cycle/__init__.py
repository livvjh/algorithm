# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


root = ListNode(1)
second = ListNode(2)
root.next = second


# head = [1,2], pos = 0
class Solution:
    @staticmethod
    def has_cycle(head: Optional[ListNode]) -> bool:
        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if fast_node == slow_node:
                return True
        else:
            return False


print(Solution.has_cycle(root))

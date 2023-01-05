# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


root_node = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

root_node.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5


class Solution:
    @staticmethod
    def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node.val


print(Solution.middle_node(root_node))

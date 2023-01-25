from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


root_node = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(2)
# node_4 = ListNode(1)

root_node.next = node_2

node_2.next = node_3


# node_3.next = node_4


class Solution:
    @staticmethod
    def is_palindrome(head: Optional[ListNode]) -> bool:
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        if result != result[::-1]:
            return False
        return True


print(Solution.is_palindrome(root_node))

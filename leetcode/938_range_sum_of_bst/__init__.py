# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root_node = TreeNode(10)
node_5 = TreeNode(5)
node_15 = TreeNode(15)
node_3 = TreeNode(3)
node_7 = TreeNode(7)
node_none = TreeNode(None)
node_18 = TreeNode(18)
root_node.left = node_5
root_node.right = node_15
node_5.left = node_3
node_5.right = node_7
node_15.right = node_18


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        stack.append(root)
        result = 0
        while stack:
            current_node = stack.pop()
            if current_node:
                if low <= current_node.val <= high:
                    result += current_node.val
                if low < current_node.val:  # 5
                    stack.append(current_node.left)
                if high > current_node.val:  # 15
                    stack.append(current_node.right)
        return result


print(Solution().range_sum_bst(root_node, 7, 15))

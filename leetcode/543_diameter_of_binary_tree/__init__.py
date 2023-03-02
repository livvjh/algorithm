from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root_2 = TreeNode(2)
root_3 = TreeNode(3)
root_4 = TreeNode(4)
root_5 = TreeNode(5)
root.left = root_2
root.right = root_3
root_2.left = root_4
root_2.right = root_5


class Solution:
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_result = max(self.max_result, left + right)
        return max(left, right) + 1

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        self.max_result = 0
        self.dfs(root)
        return self.max_result


print(Solution().diameter_of_binary_tree(root))

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p_node = TreeNode(1)
p_l_node = TreeNode(2)
p_r_node = TreeNode(3)
p_node.left = p_l_node
p_node.right = p_r_node
q_node = TreeNode(1)
q_l_node = TreeNode(2)
q_r_node = TreeNode(3)
q_node.left = p_l_node
q_node.right = p_r_node


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        max_queue_size = 0
        queue = deque([(p, q)])
        while queue:
            max_queue_size = max(max_queue_size, len(queue))
            p, q = queue.popleft()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val):
                return False
            queue.extend([(p.left, q.left), (p.right, q.right)])
        print(max_queue_size)
        return True


print(Solution().is_same_tree(p_node, q_node))

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
        p_visited = []
        p_visited_val = []
        q_visited = []
        q_visited_val = []
        if not p and not q:
            return True

        queue = deque([p])
        while queue:
            n = queue.popleft()
            if n not in p_visited:
                p_visited.append(n)
                p_visited_val.append(n.val if n is not None else None)
                queue.append(p.left)
                queue.append(p.right)

        print(p_visited_val)
        queue = deque([q])
        while queue:
            n = queue.popleft()
            if n not in q_visited:
                q_visited.append(n)
                q_visited_val.append(n.val if n is not None else None)
                queue.append(q.left)
                queue.append(q.right)
        print(q_visited_val)
        return p_visited_val == q_visited_val


print(Solution().is_same_tree(p_node, q_node))

from collections import defaultdict, deque
from typing import List


class Solution:
    def valid_path(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(set)
        stack = deque()
        visited = set()
        for n1, n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)
        visited.add(source)
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for x in neighbors[node]:
                if x not in visited:
                    visited.add(x)
                    stack.append(x)
        return False


# print(Solution().valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(Solution().valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

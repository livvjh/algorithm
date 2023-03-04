from collections import defaultdict, deque
from typing import List


class Solution:
    def valid_path(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)  # [dict:list]
        stack = deque()
        visited = list()
        for n1, n2 in edges:  # 연결을 위해 각각 add
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        # temp = dict() # 위 로직과 같음
        # neighbors = []
        # for i, v in enumerate(edges):
        #     temp[i] = v
        # neighbors.append(temp)

        visited.append(source)  # 방문 여부 체크
        stack.append(source)  # 시작점 stack 추가

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for x in neighbors[node]:
                if x not in visited:
                    visited.append(x)
                    stack.append(x)
        return False


print(Solution().valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
# print(Solution().valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

from typing import List


class Solution:
    def find_content_children(self, g: List[int], s: List[int], tt) -> int:
        g.sort()
        s.sort()

        child = 0
        for cookie in s:
            if cookie >= g[child]:
                child += 1

            if child == len(g):  # 전체 순회 조건 (결과값은 g의 전체 길이를 넘을 수 없다)
                return child

        return child


print(Solution().find_content_children([1, 2], [1, 2, 3]))

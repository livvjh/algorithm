from typing import List


class Solution:
    @staticmethod
    def weakest_rows(mat: List[List[int]], k: int) -> List[int]:
        mat_info = {}
        for key, value in enumerate(mat):
            mat_info[key] = value.count(1)
        result_datas = sorted(mat_info.items(), key=lambda item: item[1])[:k]
        return [data[0] for data in result_datas]


print(Solution.weakest_rows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3))

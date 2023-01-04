from typing import List


# 순서를 나열해서 주어진 k값까지만 배열로 리턴 (순서가 같으면 그냥 처음 주어진 배열 순으로 리턴)

class Solution:
    @staticmethod
    def weakest_rows(mat: List[List[int]], k: int) -> List[int]:
        mat_info = {}
        for key, value in enumerate(mat):
            mat_info[key] = value.count(1)
        result_datas = sorted(mat_info.items(), key=lambda item: item[1])[:k]
        return [data[0] for data in result_datas]


print(Solution.weakest_rows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3))

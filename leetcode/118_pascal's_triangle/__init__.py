from typing import List


class Solution:
    """ 1로 배열 초기화 후 반복하면서 더한 값을 구한다"""

    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            row = [1] * i  # 1로 된 배열을 만들고 그 중간 계산 값을 변경
            for j in range(1, i - 1):
                row[j] = result[i - 2][j] + result[i - 2][j - 1]
            result.append(row)
        return result


print(Solution().generate(3))

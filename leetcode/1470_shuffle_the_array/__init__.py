from typing import List


class Solution:
    """ 배열과 중간 index n이 주어지고 two pointer 개념"""

    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        left_nums = nums[0:n]
        right_nums = nums[n:]
        result = []
        for i in range(n):
            result.append(left_nums[i])
            result.append(right_nums[i])
        return result


print(Solution.shuffle([2, 5, 1, 3, 4, 7], 3))

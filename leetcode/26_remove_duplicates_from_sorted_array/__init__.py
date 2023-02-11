from typing import List


class Solution:
    """ 주어진 배열을 중복 요소 제거, 주어진 순서 그대로 유지 """

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        result_length = len(nums)
        return result_length


print(Solution.remove_duplicates([1, 1, 2]))
print(Solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

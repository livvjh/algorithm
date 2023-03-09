import math
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        max_sum_num, result = -math.inf, 0
        for i, v in enumerate(nums):
            result = max(result + v, v)
            max_sum_num = max(result, max_sum_num)
        return max_sum_num

# print(Solution().max_sub_array([5, 4, -1, 7, 8]))
# print(Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().max_sub_array([-2,-1]))
# 5
# {5, 4} {4}
# {5, 4, -1} {4, -1} {-1}

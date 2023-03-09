import math
from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        # 연속된 배열의 최대값의 곱을 반환
        # multiple_num = nums[0]
        # temp_num = nums[0]
        # if len(nums) > 1:
        #     for i in range(1, len(nums)):
        #         temp_num *= nums[i]
        #         multiple_num = max(multiple_num, temp_num)
        #         multiple_num = max(multiple_num, nums[i])
        # return multiple_num
        n = len(nums)
        max_product = [nums[0]] * n
        min_product = [nums[0]] * n

        for i in range(1, n):
            # 반복하면서 현재의 nums[i] 값과 이전의 연산된 max와 min 값들과 함께 비교하며 append (max와 min을 나누는 이유 -> 음수끼리의 연산때문 -> 음수일 경우 가장 클수도 있음)
            max_v = max_product[i - 1] * nums[i]
            min_v = min_product[i - 1] * nums[i]
            max_product[i] = max(nums[i], max_product[i - 1] * nums[i], min_product[i - 1] * nums[i])
            min_product[i] = min(nums[i], max_product[i - 1] * nums[i], min_product[i - 1] * nums[i])

        return max(max_product)


# print(Solution().max_product([2, 3, -2, 4]))
# print(Solution().max_product([-3, -1, -1]))
# print(Solution().max_product([-2]))
# print(Solution().max_product([0, 2]))
# print(Solution().max_product([-2, 0, -1]))
# print(Solution().max_product([-4,-3]))
# print(Solution().max_product([3, -1, 4]))
print(Solution().max_product([2, -5, -2, -4, 3]))

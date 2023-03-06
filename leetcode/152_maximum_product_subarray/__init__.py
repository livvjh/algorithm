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
        max_product = [nums[0]]*n
        min_product = [nums[0]]*n

        for i in range(1, n):
            max_product[i] = max(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])
            min_product[i] = min(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])

        return max(max_product)




# print(Solution().max_product([2, 3, -2, 4]))
# print(Solution().max_product([-3, -1, -1]))
# print(Solution().max_product([-2]))
# print(Solution().max_product([0, 2]))
# print(Solution().max_product([-2, 0, -1]))
# print(Solution().max_product([-4,-3]))
# print(Solution().max_product([3, -1, 4]))
print(Solution().max_product([2,-5,-2,-4,3]))

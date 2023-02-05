from typing import List


# 1회 풀이
class Solution:
    @staticmethod
    def pivot_index(nums: List[int]) -> int:

        def sum_recursion(nums: List[int], pivot: int) -> int:
            left_nums = nums[:pivot]
            right_nums = nums[pivot + 1:]
            left_val = sum(left_nums)
            right_val = sum(right_nums)
            if right_val != left_val and right_val > left_val:
                return None
            elif right_val != left_val and right_val < left_val:
                return None
            elif right_val == left_val:
                return pivot

        result_pivot = None
        for i in range(len(nums)):
            result_pivot = sum_recursion(nums, i)
            if result_pivot is not None:
                break
            if i == len(nums) - 1:
                return -1

        return result_pivot


# print(Solution.pivot_index([2, 1, -1]))
# print(Solution.pivot_index([1, 2, 3]))
# print(Solution.pivot_index([1, 7, 3, 6, 5, 6]))
print(Solution.pivot_index([-1, -1, 0, 1, 1, 0]))


# 2회 풀이
class Solution2:
    @staticmethod
    def pivot_index(nums: List[int]) -> int:
        sum_nums = sum(nums)
        left_sum = 0
        for index, val in enumerate(nums):
            if left_sum == (sum_nums - left_sum - val):
                return index
            left_sum += val
        return -1


print(Solution2.pivot_index([-1, -1, 0, 1, 1, 0]))

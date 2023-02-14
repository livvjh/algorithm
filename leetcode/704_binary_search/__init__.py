from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

        # dict
        # temp_dict = {}
        # for i, v in enumerate(nums):
        #     temp_dict[v] = i
        # print(temp_dict.get(target))
        # return temp_dict[target] if temp_dict.get(target) is not None else -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
# print(Solution().search([5], 6))

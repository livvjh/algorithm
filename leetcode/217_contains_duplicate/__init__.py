from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num_dict.get(num):
                return True
            else:
                num_dict[num] = 1
        return False

    def contains_duplicate_2(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        origin_nums = len(nums)
        unique_nums = len(set_nums)
        if origin_nums == unique_nums:
            return False
        return True


print(Solution().contains_duplicate([1, 2, 3, 4]))
print(Solution().contains_duplicate([1, 2, 3, 1]))
print(Solution().contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

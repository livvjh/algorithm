from typing import List


# 1회 풀이 (brute force)
class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        if len(nums) > 1:
            result = []
            if len(nums) == 2 and sum(nums) == target:
                return [0, 1]
            for i in range(len(nums)):
                temp_list = nums.copy()
                root = nums[i]
                del temp_list[i]
                for j in range(len(temp_list)):
                    if target == root + temp_list[j]:
                        result.append(i)
                        result.append(j + 1)
                        return result


# 2회 풀이 (dict map)
class Solution2:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            find_key = target - nums[i]
            if find_key in nums_dict and nums_dict[find_key] != i:
                return [i, nums_dict[find_key]]


print(Solution2.two_sum([3, 3], 6))

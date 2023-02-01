from typing import List


class Solution:
    @staticmethod
    def running_sum(nums: List[int]) -> List[int]:
        total = 0
        result = []
        for num in nums:
            total += num
            result.append(total)
        return result


print(Solution.running_sum([1, 2, 3, 4]))

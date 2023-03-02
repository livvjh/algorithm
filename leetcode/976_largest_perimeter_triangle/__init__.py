from typing import List


class Solution:
    def largest_perimeter(self, nums: List[int]) -> int:
        #  a + b > c
        nums.sort()
        size = len(nums)
        result = 0
        for i in range(size - 3, -1, -1):  # 큰 수 찾으면 그냥 break return (reversed로 반복)
            if nums[i] + nums[i + 1] > nums[i + 2]:
                result = nums[i] + nums[i + 1] + nums[i + 2]
                break
        return result


print(Solution().largest_perimeter([2, 1, 2]))

# print(Solution().largest_perimeter([1, 4, 18, 3, 8, 4, 4]))
# print(Solution().largest_perimeter([1, 2, 1, 10]))
# print(Solution().largest_perimeter([3, 2, 3, 4]))
# print(Solution().largest_perimeter([3, 6, 2, 3]))

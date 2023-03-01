from typing import List


class Solution:
    def largest_perimeter(self, nums: List[int]) -> int:
        #  a + b > c
        nums.sort()
        print(nums)
        index, result = 0, 0
        while index + 2 < len(nums):
            triangle = nums[index:index + 3]
            if triangle[0] + triangle[1] >= triangle[2]:
                index += 1
                result = sum(triangle)
            else:
                return result
        return result

    # print(Solution().largest_perimeter([2, 1, 2]))


print(Solution().largest_perimeter([1, 4, 18, 3, 8, 4, 4]))
# print(Solution().largest_perimeter([1, 2, 1, 10]))
# print(Solution().largest_perimeter([3, 2, 3, 4]))
# print(Solution().largest_perimeter([3, 6, 2, 3]))

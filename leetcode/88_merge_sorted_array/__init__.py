from typing import List


class Solution:
    """ nums1에 빈 리스트에 nums2를 머지하면서 정렬하기 """

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last_index = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last_index] = nums2[n - 1]
                n -= 1
            else:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            last_index -= 1

        while n > 0:
            nums1[last_index] = nums2[n - 1]
            n, last_index = n - 1, last_index - 1
        return nums1


# print(Solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
# print(Solution.merge([1], 1, [], 0))
# print(Solution.merge([0], 0, [1], 1))

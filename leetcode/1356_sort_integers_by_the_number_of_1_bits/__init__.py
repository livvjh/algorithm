from typing import List


class Solution:
    def check(self, val):
        result = 0
        while val > 0:
            if val % 2 == 1:
                result += 1
            val = val >> 1  # val = val // 2 같은 의미
        return result

    def sort_by_bits(self, arr: List[int]) -> List[int]:

        temp_dict = {}
        for a in arr:
            ones = self.check(a)
            temp_dict[a] = ones
        return sorted(arr, key=lambda x: (temp_dict[x], x))  # (dict의 value 낮은 순, key 값 순)


print(Solution().sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]))

#
# a = 0b1
# print('a = ', a)
# a = a << 1  # * 2
# print('a = ', a)
# a = a << 1  # * 2
# print('a = ', a)
# a = a << 3  # * 2**3
# print('a = ', a)
#
# a = a >> 1  # / 2
# print('a = ', a)
# a = a >> 1  # / 2
# print('a = ', a)
# a = a >> 2  # / 2**2
# print('a = ', a)

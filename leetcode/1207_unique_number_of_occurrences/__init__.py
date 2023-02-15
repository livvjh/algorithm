from typing import List


class Solution:
    def unique_occurrences(self, arr: List[int]) -> bool:
        # 주어진 배열의 값의 갯수가 고유하거나 그렇지 않으면 false
        # 고유하지 않으면 true
        set_arr = set(arr)
        if len(arr) == len(set_arr):
            return False
        return True


print(Solution().unique_occurrences([1, 2, 2, 1, 1, 3]))
print(Solution().unique_occurrences([1, 2]))
print(Solution().unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

from typing import List


class Solution:
    def unique_occurrences(self, arr: List[int]) -> bool:
        # 주어진 배열의 count가 unique한지 체크
        # unique면 true else false
        temp_dict = {}
        for i,v in enumerate(arr):
            if temp_dict.get(v):
                temp_dict[v] += 1
            else:
                temp_dict[v] = 1
        count_list = temp_dict.values()
        set_count_list = set(count_list)
        if len(count_list) == len(set_count_list):
            return True
        return False


print(Solution().unique_occurrences([1, 2, 2, 1, 1, 3]))
print(Solution().unique_occurrences([1, 2]))
print(Solution().unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

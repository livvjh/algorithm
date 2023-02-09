from typing import List


class Solution:
    """ 주어진 문자열 배열중 가장 긴 공통 접두사 문자열 없으면 빈문자열 리턴 """
    """ horizontal scan """

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        prefix = ''
        temp = strs[0]

        if not strs:
            return prefix
        for i in range(len(temp)):
            char = temp[i]
            for j in range(1, len(strs)):
                next_str = strs[j]
                if i == len(next_str) or next_str[i] != char:
                    return prefix
            prefix += char
        return prefix


# print(Solution.longest_common_prefix(['flower', 'flow', 'flight']))
# print(Solution.longest_common_prefix(["dog", "racecar", "car"]))
print(Solution.longest_common_prefix(["cir", "car"]))
print('-------')
# print(Solution.longest_common_prefix([""]))
# print(Solution.longest_common_prefix(["aa", 'aa']))
# print(Solution.longest_common_prefix(["a"]))
# print(Solution.longest_common_prefix(["",""]))

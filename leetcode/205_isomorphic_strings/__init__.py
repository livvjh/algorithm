class Solution:
    @staticmethod
    def is_isomorphic(s: str, t: str) -> bool:
        s_dict = {}
        s_list = []
        t_dict = {}
        t_list = []
        for index, str_val in enumerate(s):
            if str_val not in s_dict:
                s_dict[str_val] = index
            s_list.append(str(s_dict[str_val]))

        for index, str_val in enumerate(t):
            if str_val not in t_dict:
                t_dict[str_val] = index
            t_list.append(str(t_dict[str_val]))
        if s_list == t_list:
            return True
        return False


print(Solution.is_isomorphic('paper', 'title'))
# print(Solution.is_isomorphic('bbbaaaba', 'aaabbbba'))

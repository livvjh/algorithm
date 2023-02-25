class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # s_demo = sorted(s)
        # t_demo = sorted(t)
        # return s_demo == t_demo
        # 다른 방법이 있을까?
        if len(s) != len(t):
            return False

        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            else:
                s_dict[char] -= 1
        return True


# print(Solution().is_anagram('anagram', 'nagaram'))
print(Solution().is_anagram('ab', 'a'))

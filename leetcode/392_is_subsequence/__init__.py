class Solution:
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        """ 키워드 value == s[len(sub)] """
        sub = ''
        for index, value in enumerate(t):
            if value in s and value == s[len(sub)]:
                sub += value
        return sub == s


print(Solution.is_subsequence('ab', 'baab'))

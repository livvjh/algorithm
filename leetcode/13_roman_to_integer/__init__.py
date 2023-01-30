class Solution:
    @staticmethod
    def roman_to_int(val: str) -> int:
        result = 0
        str_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(val) - 1):
            current_num = str_dict[val[i]]
            next_num = str_dict[val[i + 1]]
            if current_num < next_num:  # 알파벳의 크기 비교로 처리 (1000 - 100)
                result -= current_num
            else:
                result += current_num
        return result + str_dict[val[-1]]


print(Solution.roman_to_int("MCMXCIV"))

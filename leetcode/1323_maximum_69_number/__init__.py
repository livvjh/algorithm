class Solution:
    @staticmethod
    def maximum_69_number(num: int) -> int:
        # num_string = str(num)
        # return int(num_string.replace('6', '9', 1))

        result = []
        num_list = [n for n in str(num)]
        if num == 9999 or num == 999 or num == 99 or num == 9:
            return num
        for i, v in enumerate(num_list):
            temp_list = num_list[:]
            if v == '6':
                temp_list[i] = '9'
            else:
                temp_list[i] = '6'
            result.append(''.join(temp_list))
        return int(max(result))


print(Solution.maximum_69_number(9669))

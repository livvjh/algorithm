class Solution:
    @staticmethod
    def number_of_steps(num: int) -> int:
        count = 0
        if num == 0:
            return 0
        while True:
            count += 1
            if num % 2 == 1:
                num -= 1
            else:
                num = num // 2
            if num == 1:
                count += 1
                return count


print(Solution.number_of_steps(123))

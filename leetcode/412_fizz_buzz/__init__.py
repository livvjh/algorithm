from typing import List


class Solution:
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        result = []
        if 1 <= n <= 10000:
            for i in range(1, n+1):
                if i % 3 == 0 and i % 5 != 0:
                    result.append('Fizz')
                elif i % 5 == 0 and i % 3 != 0:
                    result.append("Buzz")
                elif i % 5 == 0 and i % 3 == 0:
                    result.append("FizzBuzz")
                else:
                    result.append(str(i))

        return result


print(Solution.fizz_buzz(3))

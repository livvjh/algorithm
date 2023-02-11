import itertools


class Solution:
    """ DP 주어진 n에 따라 앞에 누적된 계산을 그대로 사용해야 한다 """

    @staticmethod
    def climb_stairs(n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

    @staticmethod
    def climb_stairs_2(n: int) -> int:
        steps_dict = {1: 1, 2: 2}
        for i in range(3, n + 1):
            steps_dict[i] = steps_dict[i-1] + steps_dict[i - 2] # 누적 값을 통해 계산
        return steps_dict[n]

print(Solution.climb_stairs_2(4))

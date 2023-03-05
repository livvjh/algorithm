from functools import reduce
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        # 내가 푼 풀이법
        except_nums = []
        result = []
        for i, v in enumerate(nums):
            num_list = nums.copy()
            del num_list[i]
            except_nums.append(num_list)
        for except_num in except_nums:
            result.append(reduce(lambda x, y: x * y, except_num))  # 여기서 이미 n2
        return result

    def product_except_self_solve(self, nums: List[int]) -> List[int]:
        multiple_num, zero_count = reduce(lambda a, b: a * (b if b else 1), nums, 1), nums.count(0)
        if zero_count == len(nums):
            return nums
        for i, v in enumerate(nums):
            if zero_count > 1:  # 핵심 1 -> 0이 1개 이상이면 해당 인덱스외 다른 인덱스에 0이 있기에 곱해도 어차피 0
                nums[i] = 0
            elif zero_count == 1:  # 핵심 2 -> 0이 있으면 연산 필요가 없기에 그대로 0으로 반환
                nums[i] = 0 if v else multiple_num
            else:
                nums[i] = multiple_num // v  # 핵심 3 -> multiple_num에서 각 해당 타겟의 값으로 몫이 구하는 값
        return nums


# print(Solution().product_except_self([-1, 1, 0, -3, 3]))
print(Solution().product_except_self_solve([-1, 1, 0, -3, 3]))
# print(Solution().product_except_self_solve([0, 4, 0]))
print(Solution().product_except_self_solve([0, 0]))
# print(Solution().product_except_self([1, 2, 3]))

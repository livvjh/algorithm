from typing import List


class Solution:
    @staticmethod
    def maximum_wealth(accounts: List[List[int]]) -> int:
        max_value = 0
        for account in accounts:
            sum_account = sum(account)
            if max_value < sum_account:
                max_value = sum_account
        return max_value


print(Solution.maximum_wealth([[1, 5], [7, 3], [3, 5]]))

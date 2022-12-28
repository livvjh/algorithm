from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for account in accounts:
            sum_account = sum(account)
            if max_value < sum_account:
                max_value = sum_account
        return max_value


print(Solution().maximumWealth([[1,5],[7,3],[3,5]]))

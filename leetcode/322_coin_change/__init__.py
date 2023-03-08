import math
from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    dp[cur_amount] = min(dp[cur_amount], 1 + dp[cur_amount - coin])

        return dp[amount] if dp[amount] != math.inf else -1


# print(Solution().coin_change([1, 2, 5], 11))
# print(Solution().coin_change([2], 3))
# print(Solution().coin_change([1], 0))
print(Solution().coin_change([2, 5, 10, 1], 27))
# print(Solution().coin_change([186, 419, 83, 408], 6249))

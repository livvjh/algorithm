from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 무한 값
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


print(Solution().max_profit([7, 1, 5, 3, 6, 4]))
# print(Solution().max_profit([7, 6, 4, 3, 1]))
# print(Solution().max_profit([1]))
# print(Solution().max_profit([1, 2]))
# print(Solution().max_profit([1, 4, 2]))
# print(Solution().max_profit([2, 4, 1]))

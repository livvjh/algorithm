from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]


print(Solution().count_bits(5))

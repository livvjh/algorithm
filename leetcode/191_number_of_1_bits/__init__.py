class Solution:
    def hamming_weight(self, n: int) -> int:
        return bin(n).count('1')


print(Solution().hamming_weight(11111111111111111111111111111101))

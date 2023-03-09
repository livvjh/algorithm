class Solution:

    def count_odds(self, low: int, high: int) -> int:
        odd = (high - low) // 2  # 숫자 합과 사이에 2로 나눈 몫이 홀수 갯수

        if low % 2 == 1 or high % 2 == 1:  # inclusive add 1
            odd += 1

        return odd
        # nums = list(filter(lambda x: x % 2 == 1, range(low, high + 1)))
        # return len(nums) # Time Limit Exceeded


print(Solution().count_odds(3, 7))
print(Solution().count_odds(8, 10))

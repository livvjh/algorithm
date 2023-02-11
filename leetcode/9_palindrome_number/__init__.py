class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        x_str = str(x)
        reverse_str = list(reversed(x_str))
        if list(x_str) == reverse_str:
            return True
        return False


print(Solution.is_palindrome(123))
print(Solution.is_palindrome(121))

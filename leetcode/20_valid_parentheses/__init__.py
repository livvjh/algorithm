class Solution:
    def is_valid(self, s: str) -> bool:
        stack_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in stack_dict:
                top_elem = stack.pop() if stack else '!'
                if stack_dict[char] != top_elem:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

        # while "()" in s or "{}" in s or '[]' in s:
        #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # return s == ''




print(Solution().is_valid("()"))
print(Solution().is_valid("()[]{}"))
print(Solution().is_valid("(]"))
print(Solution().is_valid("["))
# print(Solution().is_valid("((()(())))"))

class Linter:
    def __init__(self):
        self.stack = []
        self.error = "success"

    def opening_brace(self, char):
        return char in ['(', '[', '{']

    def closing_brace(self, char):
        return char in [')', ']', '}']

    def opening_brace_of(self, char):
        return {')': '(', ']': '[', '}': '{'}[char]

    def most_recent_opening_brace(self):
        return self.stack[-1] if self.stack else None

    def closes_most_recent_opening_brace(self, char):
        return self.opening_brace_of(char) == self.most_recent_opening_brace()

    def lint(self, text):
        for index, char in enumerate(text):
            if self.opening_brace(char):
                self.stack.append(char)
            elif self.closing_brace(char):
                if self.closes_most_recent_opening_brace(char):
                    self.stack.pop()
                else:
                    self.error = f"Incorrect closing brace: {char} at index {index}"
                    return

        if self.stack:
            self.error = f"{self.stack[-1]} does not have a closing brace"


linter = Linter()
# print(linter.lint("( var x = { y: [1, 2, 3]) } "))
# print(linter.error)
# print(linter.lint("( var x = { y: [1, 2, 3] } "))
# print(linter.error)
print(linter.lint("( var x = { y: [1, 2, 3] } )"))
print(linter.error)

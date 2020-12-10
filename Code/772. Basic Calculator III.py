# calculator III solution based on bilibili explanation
class Solution:
    i = 0
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        num = 0
        while self.i < len(s):
            c = s[self.i]
            self.i += 1
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(':
                num = self.calculate(s)
            if self.i >= len(s) or c in ['+', '-', '*', '/', ')']:
                if operator == '+':
                    stack.append(num)
                if operator == '-':
                    stack.append(-num)
                if operator == '*':
                    stack.append(stack.pop() * num)
                if operator == '/':
                    previous = stack.pop()
                    if previous / num > 0:
                        stack.append(previous // num)
                    else:
                        stack.append(-(abs(previous) // abs(num)))
                operator = c
                num = 0
            if c == ')':
                break
        return sum(stack)
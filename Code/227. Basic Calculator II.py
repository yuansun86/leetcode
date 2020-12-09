class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        value = 0
        s = s.replace(' ', '')
        for i in range(len(s)):
            if s[i].isdigit():
                value = value * 10 + int(s[i])
            if i == len(s) - 1 or s[i] in ['+', '-', '*', '/']:
                if sign == '+':
                    stack.append(value)
                if sign == '-':
                    stack.append(-value)
                if sign == '*':
                    previous = stack.pop()
                    stack.append(previous * value)
                if sign == '/':
                    previous = stack.pop()
                    if previous // value >= 0:
                        stack.append(previous // value)
                    else:
                        stack.append(-(abs(previous) // abs(value)))
                sign = s[i]
                value = 0
        return sum(stack)
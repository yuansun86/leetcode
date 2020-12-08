class Solution:
    def calculate(self, s: str) -> int:
        def evaluateStack(stack):
            result = stack.pop() if stack else 0
            while stack and stack[-1] != ')':
                sign = stack.pop()
                if sign == '+':
                    result += stack.pop()
                elif sign == '-':
                    result -= stack.pop()
            return result
        
        stack = []
        s = '(' + s + ')'
        n, operand = 0, 0 
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                operand = operand + int(s[i]) * 10 ** n
                n += 1
            elif s[i] != ' ':
                if n != 0:
                    stack.append(operand)
                    n, operand = 0, 0
                if s[i] == '(':
                    temp = evaluateStack(stack)
                    stack.pop()
                    stack.append(temp)
                else:
                    stack.append(s[i])
        return evaluateStack(stack)
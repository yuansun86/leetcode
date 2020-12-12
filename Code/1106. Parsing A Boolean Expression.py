class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in range(len(expression)):
            ch = expression[i]
            if ch == ',':
                continue
            elif ch == 't':
                stack.append(True)
            elif ch == 'f':
                stack.append(False)
            elif ch in [ '(', '!',  '|', '&']:
                stack.append(ch)
            elif i == len(expression) - 1 or ch == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == '!':
                    stack.append(not temp[0])
                elif operator == '&':
                    result = True
                    for boolean in temp:
                        result = result and boolean
                    stack.append(result)
                elif operator == '|':
                    result = False
                    for boolean in temp:
                        result = result or boolean
                    stack.append(result)
        return stack[0]
                    
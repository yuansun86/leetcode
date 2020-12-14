from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        while i < len(formula):
            ch = formula[i]
            if ch == '(':
                stack.append(Counter())
                i += 1
            elif ch == ')':
                recent_counter = stack.pop()
                i += 1
                multiple_left = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                if multiple_left == i:
                    multiple = 1
                else:
                    multiple = int(formula[multiple_left:i])
                for atom, count in recent_counter.items():
                    stack[-1][atom] += count * multiple
            else:
                element_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                element = formula[element_start:i]
                count_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                if count_start == i:
                    element_count = 1
                else:
                    element_count = int(formula[count_start:i])
                stack[-1][element] += element_count
        result = sorted(list(stack[0].items()))
        output = []
        for atom, count in result:
            if count == 1:
                output.append(atom)
            else:
                output.append(atom + str(count))
        return ''.join(output)
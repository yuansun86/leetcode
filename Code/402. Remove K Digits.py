class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)

        if k == 0:
            return ''.join(numStack).lstrip('0') or '0'
        else:
            return ''.join(numStack[:-k]).lstrip('0') or '0'
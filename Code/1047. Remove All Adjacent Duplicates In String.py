# To remove adjacent duplicates in a string, so only compare two adjacent
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        i = 0
        length = len(S)
        while i < length:
            character = S[i]
            if not stack or character != stack[-1]:
                stack.append(character)
            else:
                stack.pop()
            i += 1
        return ''.join(stack)
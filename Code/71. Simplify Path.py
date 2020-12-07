# if encounter '.', just skip.
# if encounter '.., skip the upper level'

class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        stack = []
        for item in p:
            if not stack:
                if item == '' or item == '.' or item == '..':
                    continue
                else:
                    stack.append(item)
            else:
                if item == '' or item == '.':
                    continue
                elif item == '..':
                    stack.pop()
                else:
                    stack.append(item)
        return '/' + '/'.join(stack)
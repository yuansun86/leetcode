import re
class Solution:
    def expand(self, S: str) -> List[str]:
        t = re.split(r'[{}]', S)
        pool = []
        for item in t:
            if item:
                pool.append(item.split(','))
        
        def helper(lst, index, target, current, result):
            if index == target:
                result.append(''.join(current))
            else:
                for ch in lst[index]:
                    current.append(ch)
                    helper(lst, index + 1, target, current, result)
                    current.pop()
        
        result = []
        helper(pool, 0, len(pool), [], result)
        return sorted(result)
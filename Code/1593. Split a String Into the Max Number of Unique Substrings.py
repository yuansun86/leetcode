class Solution:
    ans = 0
    def maxUniqueSplit(self, s: str) -> int:
        self.helper(s, 0, set())
        return self.ans
    
    def helper(self, s, index, used):
        if index >= len(s):
            self.ans = max(self.ans, len(used))
            return
        
        for i in range(index + 1, len(s) + 1):
            prefix = s[index:i]
            if prefix in used:
                continue
            used.add(prefix)
            self.helper(s, i, used)
            used.remove(prefix)
            
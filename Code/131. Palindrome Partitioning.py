class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.backtracking(s, 0, [], results)
        return results
    
    def isPar(self, s):
        if not s or len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
    def backtracking(self, s, index, path, results):
        if index == len(s):
            results.append(path[:])
            return
        for i in range(index + 1, len(s) + 1):
            prefix = s[index : i]
            if self.isPar(prefix):
                path.append(prefix)
                self.backtracking(s, i, path, results)
                path.pop()
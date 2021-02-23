class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.backtracking(n, 0, 0, [], results)
        return results
    
    def backtracking(self, n, left, right, path, results):
        if left > n or right > n:
            return 
        if left == n and right == n:
            results.append(''.join(path))
            return
        path.append('(')
        self.backtracking(n, left + 1, right, path, results)
        path.pop()
        if left > right:
            path.append(')')
            self.backtracking(n, left, right + 1, path, results)
            path.pop()
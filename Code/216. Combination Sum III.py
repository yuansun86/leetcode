class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        self.backtracking(0, k, n, [], results)
        return results
    
    def backtracking(self, index, k, n, path, results):
        if k == 0:
            if n == 0:
                results.append(path[:])
            return
            
        
        for i in range(index + 1, 10):
            path.append(i)
            self.backtracking(i, k - 1, n - i, path, results)
            path.pop()
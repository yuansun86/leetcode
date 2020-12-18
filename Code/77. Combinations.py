class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, start, current, result):
            if k == 0:
                result.append(current[::])
                return
            for i in range(start, n + 1):
                current.append(i)
                backtracking(n, k - 1, i + 1, current, result)
                current.pop()
        
        result = []
        backtracking(n, k, 1, [], result)
        return result
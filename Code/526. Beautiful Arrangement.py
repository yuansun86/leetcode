class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (1 + n)
        results = [0]
        self.backtracking(n, visited, 1, [], results)
        return results[0]
    
    def backtracking(self, n, visited, index, path, results):
        if index == n + 1:
            results[0] += 1
            return
        for i in range(1, n + 1):
            if visited[i] == True:
                continue
            if i % index == 0 or index % i == 0:
                visited[i] = True
                self.backtracking(n, visited, index + 1, path, results)
                visited[i] = False

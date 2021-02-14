class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = []
        self.dfs(0, [], results, S)
        return results
    
    def dfs(self, index, path, results, S):
        if index == len(S):
            results.append(''.join(path))
            return
        
        ch = S[index]
        if not ch.isalpha():
            path.append(ch)
            self.dfs(index + 1, path, results, S)
            path.pop()
        else:   
            path.append(ch.upper())
            self.dfs(index + 1, path, results, S)
            path.pop()

            path.append(ch.lower())
            self.dfs(index + 1, path, results, S)
            path.pop()
            
            
            
        
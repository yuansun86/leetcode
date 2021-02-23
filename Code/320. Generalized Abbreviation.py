class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        results = []
        self.backtracking(word, 0, [], results)
        return results
    
    def backtracking(self, word, index, path, results):
        if index == len(word):
            results.append(''.join(path))
            return
        
        if not path:
            for i in range(index + 1, len(word) + 1):
                path.append(word[index: i])
                self.backtracking(word, i, path, results)
                path.pop()
                path.append(str(i - index))
                self.backtracking(word, i, path, results)
                path.pop()
        elif path[-1].isalpha():
            for i in range(index + 1, len(word) + 1):
                path.append(str(i - index))
                self.backtracking(word, i, path, results)
                path.pop()
        else:
            for i in range(index + 1, len(word) + 1):
                path.append(word[index: i])
                self.backtracking(word, i, path, results)
                path.pop()
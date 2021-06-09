# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            word = random.choice(wordlist)
            res = master.guess(word)
            selected = []
            for w in wordlist:
                if self.compare(word, w) == res:
                    selected.append(w)
            wordlist = selected
        
            
        
        
    
    
    def compare(self, w1, w2):
        count = 0
        for c1, c2 in zip(w1, w2):
            if c1 == c2:
                count += 1
        return count
            
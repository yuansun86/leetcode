class Solution:
    def minWindow(self, s: str, t: str) -> str:
        j = 0
        requirement = [0] * 52
        for ch in t:
            if ch.islower():
                requirement[ord(ch) - 97] += 1
            else:
                requirement[ord(ch) - 65 + 26] += 1
        count = [0] * 52
        res = float('inf')
        ans = ""
        for i in range(len(s)):
            while j < len(s) and not self.isValid(count, requirement):
                letter = s[j]
                self.addLetter(letter, count)
                j += 1
            if not self.isValid(count, requirement):
                break
            if j - i < res:
                res = j - i
                ans = s[i:j]
            self.deleteLetter(s[i], count)
        return ans 
    
    
    
    def addLetter(self, letter, count):
        if letter.islower():
            count[ord(letter) - 97] += 1
        else:
            count[ord(letter) - 65 + 26] += 1
            
    def deleteLetter(self, letter, count):
        if letter.islower():
            count[ord(letter) - 97] -= 1
        else:
            count[ord(letter) - 65 + 26] -= 1
            
    def isValid(self, count, requirement):
        # both count and requirement are array of length 52, first half is lower, second half is upper
        for i in range(len(count)):
            if count[i] < requirement[i]:
                return False
        return True
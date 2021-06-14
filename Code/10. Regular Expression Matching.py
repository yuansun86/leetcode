class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '':
            if p == "":
                return True
            elif len(p) == 1:
                return False
            elif p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        if not p:
            return False
        
        if len(p) == 1:
            return s == p or (len(s) == 1 and p == '.')
        
        if p[1] != '*':
            if p[0] == s[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
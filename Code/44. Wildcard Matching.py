class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, {})
        
    def helper(self, s, p, d):
        if (s, p) in d:
            return d[(s, p)]
        
        if not p:
            return not s
        
        if not s:
            return p == "" or set(p) == set('*')
        
        if p[0] == '?':
            res = self.helper(s[1:], p[1:], d)
            d[(s, p)] = res
            return res
        elif p[0] == '*':
            res = self.helper(s, p[1:], d) or self.helper(s[1:], p, d)
            d[(s, p)] = res
            return res
        else:
            if not s[0] == p[0]:
                return False
            else:
                res = self.helper(s[1:], p[1:], d)
                d[(s, p)] = res
                return res
        
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def F(s, wordDict, memo):
            if not s:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            result = []
            for index in range(len(s)):
                prefix = s[:index]
                if prefix in wordDict:
                    for post_result in F(s[index:], wordDict, memo):
                        result.append([prefix] + post_result)
            if s in wordDict:
                result.append([s])
            memo[s] = result
            return result
        
        memo = {}
        result = F(s, wordDict, memo)
        results = [" ".join(item) for item in result]
        return results
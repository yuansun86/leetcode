class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def checkComb(candidates, current, remain, index, result):
            if remain < 0:
                return
            
            if remain == 0:
                result.append(current.copy())
                return
            
            for i in range(index, len(candidates)):
                if i == index or candidates[i] != candidates[i-1]:
                    current.append(candidates[i])
                    checkComb(candidates[:i]+candidates[i+1:], current, remain - candidates[i], i, result)
                    current.pop()
        
        result = []
        candidates.sort()
        checkComb(candidates, [], target, 0, result)
        return result
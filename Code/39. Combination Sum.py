class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def checkComb(candidates, current, remain, index, result):
            if remain < 0:
                return
            
            if remain == 0:
                result.append(current.copy())
                return
            
            for i in range(index, len(candidates)):
                current.append(candidates[i])
                checkComb(candidates, current, remain - candidates[i], i, result)
                current.pop()
        
        result = []
        checkComb(candidates, [], target, 0, result)
        return result
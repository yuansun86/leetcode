class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if not firstList or not secondList:
            return []
        i = 0
        j = 0
        m = len(firstList)
        n = len(secondList)
        while i < m and j < n:
            i_forward = False
            if firstList[i][0] <= secondList[j][0]:
                cur = firstList[i]
                i_forward = True
            else:
                cur = secondList[j]
                
            if not res:
                res.append(cur)
            else:
                prev = res.pop()
                if cur[0] > prev[1]:
                    res.append(cur)
                elif cur[0] == prev[1]:
                    res.append([cur[0], cur[0]])
                    res.append([cur[0], cur[1]])
                else:
                    res.append([cur[0], min(prev[1], cur[1])])
                    res.append([min(prev[1], cur[1]), max(prev[1], cur[1])])
            if i_forward:
                i += 1
            else:
                j += 1
        
        while i < m:
            cur = firstList[i]
            prev = res.pop()
            if cur[0] > prev[1]:
                res.append(cur)
            elif cur[0] == prev[1]:
                res.append([cur[0], cur[0]])
                res.append([cur[0], cur[1]])
            else:
                res.append([cur[0], min(prev[1], cur[1])])
                res.append([min(prev[1], cur[1]), max(prev[1], cur[1])])
            i += 1
        while j < n:
            cur = secondList[j]
            prev = res.pop()
            if cur[0] > prev[1]:
                res.append(cur)
            elif cur[0] == prev[1]:
                res.append([cur[0], cur[0]])
                res.append([cur[0], cur[1]])
            else:
                res.append([cur[0], min(prev[1], cur[1])])
                res.append([min(prev[1], cur[1]), max(prev[1], cur[1])])
            j += 1
        res.pop()
        return res
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        remove = toBeRemoved
        for i, iv in enumerate(intervals):
            if remove[0] <= iv[0]:
                if remove[1] < iv[0]:
                    res.extend(intervals[i:])
                    return res
                elif remove[1] >= iv[1]:
                    remove[0] = iv[1]
                else:
                    res.append([remove[1], iv[1]])
                    remove = [float('-inf'), float('-inf')]
            elif remove[0] < iv[1]:
                if remove[1] < iv[1]:
                    res.append([iv[0], remove[0]])
                    res.append([remove[1], iv[1]])
                    remove = [float('-inf'), float('-inf')]
                else:
                    res.append([iv[0], remove[0]])
                    remove = [iv[1], remove[1]]
            else:
                res.append(iv)
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        index = 0
        left, right = newInterval
        while index < len(intervals):
            if intervals[index][0] < left:
                result.append([intervals[index][0], intervals[index][1]])
                index += 1
            else:
                break
        
        if not result or result[-1][1] < left:
            result.append([left,right])
        else:
            result[-1][1] = max(result[-1][1], right)
        
        while index < len(intervals):
            if result[-1][1] < intervals[index][0]:
                result.append([intervals[index][0], intervals[index][1]])
            else:
                result[-1][1] = max(result[-1][1], intervals[index][1])
            index += 1
        return result
                
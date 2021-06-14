class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res= min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] <= height[j]:
                min_height = height[i]
                while i < j and height[i] <= min_height:
                    i += 1;
                if i < j:
                    res = max(res, min(height[i], height[j]) * (j - i))
            else:
                min_height = height[j]
                while i < j and height[j] <= min_height:
                    j -= 1
                if i < j:
                    res = max(res, min(height[i], height[j]) * (j - i))        
        return res
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        remain = K
        max_count = 0
        while right < len(A):
            if A[right] == 1:
                right += 1
            elif A[right] == 0:
                if remain > 0:
                    right += 1
                    remain -= 1
                else:
                    max_count = max(max_count, right - left)
                    if A[left] == 0:
                        remain += 1
                    left += 1
        max_count = max(max_count, right - left)
        return max_count
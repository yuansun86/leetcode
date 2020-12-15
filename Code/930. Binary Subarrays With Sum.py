class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        positions = [-1]
        for index, value in enumerate(A):
            if value:
                positions.append(index)
        positions.append(len(A))
        count = 0
        
        if S == 0:
            for i in range(1, len(positions)):
                temp_count = positions[i] - positions[i - 1] - 1
                count += temp_count * (temp_count + 1) // 2
            return count
        
        for i in range(1, len(positions) - S):
            j = i + S - 1
            left_count = positions[i] - positions[i - 1]
            right_count = positions[j + 1] - positions[j]
            count += left_count * right_count
        return count
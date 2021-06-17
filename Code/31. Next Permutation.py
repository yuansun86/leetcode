class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # from back to front, find first "ab" where a < b.
        # then find c, where c is behind or equal to b, but is smallest element > a
        # swap, a,c 
        # reverse nums[a+ 1:]


        a = None
        b = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                a = i - 1
                b = i
                break
        if a == None:
            self.reverse(nums, 0)
            return
        
        c = None
        for i in range(len(nums) - 1, a, -1):
            if nums[i] > nums[a]:
                c = i
                break
        nums[a], nums[c] = nums[c], nums[a]
        self.reverse(nums, a + 1)
        
    
    def reverse(self, nums, index):
        i = index
        j = len(nums) - 1
        while i < j :
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        
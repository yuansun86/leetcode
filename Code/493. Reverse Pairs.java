class Solution {
    public int reversePairs(int[] nums) {
        return mergeAndCount(nums, 0, nums.length - 1);
    }
    
    private int mergeAndCount(int[] nums, int start, int end){
        if (start >= end){
            return 0;
        }
        
        int mid = start + (end - start) / 2;
        int count = mergeAndCount(nums, start, mid) + mergeAndCount(nums, mid + 1, end);

        int j = mid + 1;
        for (int i = start; i <= mid; i++){
            while (j <= end && nums[i] > (long)(nums[j]) * 2){
                j++;
            }
            count += j - (mid + 1);
        }
        
        
        List<Integer> temp = new ArrayList<>();
        int left = start, right = mid + 1;
        while (left <= mid && right <= end){
            if (nums[left] <= nums[right]){
                temp.add(nums[left++]);
            }else{
                temp.add(nums[right++]);
            }
        }
        
        while (left <= mid){
            temp.add(nums[left++]);
        }
        while (right <= end){
            temp.add(nums[right++]);
        }
        
        int offset = 0;
        for (Integer number: temp){
            nums[start + offset] = number;
            offset++;
        }
        
        return count;
    }
}
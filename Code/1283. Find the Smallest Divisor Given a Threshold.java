class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int left = 0;
        int right = 0;
        for (int i = 0; i < nums.length; i++){
            right = Math.max(nums[i], right);
        }
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (divideResult(nums, mid) > threshold){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (divideResult(nums, left) <= threshold){
            return left;
        }
        if (divideResult(nums, right) <= threshold){
            return right;
        }
        return left;
    }
    
    private int divideResult(int[] nums, int div){
        int res = 0;
        for (int i = 0; i < nums.length; i++){
            res += Math.ceil(nums[i] / (div * 1.0));
        }
        return res;
    }
}
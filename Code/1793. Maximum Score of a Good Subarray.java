class Solution {
    public int maximumScore(int[] nums, int k) {
        int res = nums[k];
        int min = nums[k];
        int i = k;
        int j = k;
        while (i - 1 >= 0 || j + 1 < nums.length){
            if (i - 1 < 0){
                j++;
                min = Math.min(min, nums[j]);
                res = Math.max(res, (j - i + 1) * min);
            }else if (j + 1 >= nums.length){
                i--;
                min = Math.min(min, nums[i]);
                res = Math.max(res, (j - i + 1) * min);
            }else if (nums[i-1] >= nums[j + 1]){
                i--;
                min = Math.min(min, nums[i]);
                res = Math.max(res, (j - i + 1) * min);
            }else{
                j++;
                min = Math.min(min, nums[j]);
                res = Math.max(res, (j - i + 1) * min);  
            }
        }
        return res;
    }
}
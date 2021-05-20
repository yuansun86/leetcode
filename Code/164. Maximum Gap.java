class Solution {
    public int maximumGap(int[] nums) {
        Arrays.sort(nums);
        int res = 0;
        for (int i = 0; i < nums.length - 1; i++){
            res = Math.max(res, nums[i + 1] - nums[i]);
        }
        return res;
    }
}
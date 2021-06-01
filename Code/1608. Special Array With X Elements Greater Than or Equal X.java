class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){
            int n = nums.length - i;
            if ((nums[i] >= n) && (i == 0 || n > nums[i - 1])) return n;
        }
        return -1;
    }
}
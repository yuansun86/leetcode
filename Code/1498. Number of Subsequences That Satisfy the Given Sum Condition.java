class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int res = 0;
        int n = nums.length;
        int j = n - 1;
        int mod = (int)1e9+7;
        int[] pow = new int[n];
        pow[0] = 1;
        for (int k = 1; k < n; k++){
            pow[k] = pow[k-1] * 2 % mod;
        }
        for (int i = 0; i < n; i++){
            while (j >= i && nums[i] + nums[j] > target){
                j--;
            }
            if (i > j){
                break;
            }
            res = (res + pow[j - i]) % mod;
        }
        return res;
    }
}
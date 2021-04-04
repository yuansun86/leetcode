class Solution {
    public int splitArray(int[] nums, int m) {
        int[][] dp = new int[nums.length + 1][m + 1];
        for (int i = 0; i < nums.length + 1; i++){
            for (int j = 0; j < m + 1; j++){
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][1] = 0;
        for (int i = 1; i < nums.length + 1; i++){
            dp[i][1] = dp[i - 1][1] + nums[i - 1]; 
        }
        
        
        for (int j = 1; j < m + 1; j++){
            for (int i = 1; i < nums.length + 1; i++){
                for (int k = 0; k < i; k++){
                    int temp = Math.max(dp[k][j - 1], dp[i][1] - dp[k][1]);
                    dp[i][j] = Math.min(dp[i][j], temp);
                }
            }
        }
        return dp[nums.length][m];
    }
}
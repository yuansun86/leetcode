class Solution {
    public int maxResult(int[] nums, int k) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> b[0] - a[0]);
        pq.add(new int[]{nums[0], 0});
        for (int i = 1; i < nums.length; i++){
            while (pq.peek()[1] < i - k) pq.poll();
            dp[i] = nums[i] + pq.peek()[0];
            pq.add(new int[]{dp[i], i});
        }
        return dp[nums.length - 1];
    }
}
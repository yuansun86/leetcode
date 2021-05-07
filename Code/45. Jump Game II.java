class Solution {
    public int jump(int[] nums) {
        int steps = 0;
        int currentEnd = 0;
        int farthest = 0;
        for (int i = 0; i < nums.length - 1; i++){
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd){
                steps++;
                currentEnd = farthest;
            }
        }
        return steps;
    }
}
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Deque<Integer> leftStack = new ArrayDeque<>();
        int left = nums.length;
        int right = 0;
        for (int i = 0; i < nums.length; i++){
            while(!leftStack.isEmpty() && nums[leftStack.peekLast()] > nums[i]){
                left = Math.min(left, leftStack.pollLast());
            }
            leftStack.offerLast(i);
        }
        
        for (int i = nums.length - 1; i >= 0; i--){
            while (!rightStack.isEmpty() && nums[rightStack.peekLast()] < nums[i]){
                right = Math.max(right, rightStack.pollLast());
            }
            rightStack.offerLast(i);
        }
        
        return right - left > 0 ? right - left + 1 : 0;
    }
}
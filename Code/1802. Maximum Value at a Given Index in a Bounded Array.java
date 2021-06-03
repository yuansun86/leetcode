class Solution {
    public int maxValue(int n, int index, int maxSum) {
        long left = 0;
        long right = maxSum;
        while (left + 1 < right){
            long mid = left + (right - left) / 2;
            if (isValid(n, index, maxSum, mid)){
                left = mid;
            }else{
                right = mid;
            }
        }
        

        if (isValid(n, index, maxSum, right)) return (int)right;
        if (isValid(n, index, maxSum, left)) return (int)left;
        return 0;
    }
    
    private boolean isValid(int n, int index, int maxSum, long target){
        long left_length = index + 1;
        long right_length = n - index;
        long sum = getSum(left_length, target) + getSum(right_length, target) - target;
        return sum <= maxSum;
    }
    
    private long getSum(long length, long largest){
        long sum = 0;
        if (length <= largest){
            sum = length * (largest + largest - length + 1) / 2;
        }else{
            sum = largest * (1 + largest) / 2;
            sum += (length - largest);
        }
        return sum;
    }
}
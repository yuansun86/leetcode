class Solution {
    public int findBestValue(int[] arr, int target) {
        int left = 0; 
        int right = 0;
        for (int number : arr){
            right = Math.max(right, number);
        }
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            int sum = getSum(arr, mid);
            if (sum >= target){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        int leftGap = Math.abs(getSum(arr, left) - target);
        int rightGap = Math.abs(getSum(arr, right) - target);
        
        if (leftGap <= rightGap){
            return left;
        }else{
            return right;
        }

    }
    
    private int getSum(int[] arr, int k){
        int sum = 0;
        for (int i : arr){
            sum += i >= k? k : i;
        }
        return sum;
    }
}
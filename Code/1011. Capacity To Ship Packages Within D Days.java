class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0;
        int right = 0;
        for (int i: weights){
            left = Math.max(left, i);
            right += i;
        }
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (shipDays(weights, mid) > D){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (shipDays(weights, left) <= D){
            return left;
        }
        
        if (shipDays(weights, right) <= D){
            return right;
        }
        
        return left;
        
    }
    
    private int shipDays(int[] weights, int capacity){
        int day = 1;
        int cur = 0;
        for (int weight: weights){
            if (cur + weight > capacity){
                day++;
                cur = 0;
            }
            cur += weight;
        }
        
        return day;
    }
}
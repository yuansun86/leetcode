class Solution {
    private long mod = (int)(1e+9 + 7);
    public int maxProfit(int[] inventory, int orders) {
        int left = 0;
        int right = 0;
        for (int i : inventory){
            right = Math.max(right, i);
        }
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (isValidK(mid, inventory, orders)){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (isValidK(right, inventory, orders)){
            return getProfit(right, inventory, orders);
        }
        
        if (isValidK(left, inventory, orders)){
            return getProfit(left, inventory, orders);
        }
        return 0;
        
        
    }
    
    private boolean isValidK(int k, int[] inventory, int orders){
        long sum = 0;
        for (int i : inventory){
            if (i >= k){
                sum += (i - k + 1);
            }
        }
        return sum >= orders;
    }
    
    private int getProfit(int k, int[] inventory, int orders){
        long count = 0;
        long res = 0;
        for (int i : inventory){
            long l = i;
            if (i > k){
                long temp = (l + k + 1) * (l - k) / 2;
                res = res + temp;
                count += (l - k);
            }
        }
        
        if (orders > count){
            res = res + (orders - count) * k;
        }
        return (int)(res % mod);
    }
}
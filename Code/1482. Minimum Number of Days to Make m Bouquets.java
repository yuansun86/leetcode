class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int right = bloomDay[0];
        for (int i = 0; i < bloomDay.length; i++){
            if (bloomDay[i] > right){
                right = bloomDay[i];
            }
        }
        
        int left = 0;
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (canMake(bloomDay, m, k, mid)){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        if (canMake(bloomDay, m, k , left)){
            return left;
        }
        if (canMake(bloomDay, m, k, right)){
            return right;
        }
        return -1;
        
    }
    
    private static boolean canMake(int[] bloomDay, int m, int k, int day){
        int left = 0;
        while (left < bloomDay.length - k + 1){
            boolean valid = true;
            for (int i = 0; i < k; i++){
                if (bloomDay[left + i] > day){
                    valid = false;
                    left = left + i + 1;
                    break;
                }
            }
            if (valid == true){
                m -= 1;
                left = left + k;
            }
            if (m == 0){
                return true;
            }
        }
        return m <= 0;
    }
}
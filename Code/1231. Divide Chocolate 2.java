class Solution {
    public int maximizeSweetness(int[] sweetness, int K) {
        int left = 0;
        int right = (int)1e9;
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (validNumber(sweetness, K, mid)){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (validNumber(sweetness, K, right)) return right;
        if (validNumber(sweetness, K, left)) return left;
        return 0;
        
    }
    
    private boolean validNumber(int[] sweetness, int K, int n){
        int count = 0;
        int curSum = 0;
        for (int i = 0; i < sweetness.length; i++){
            curSum += sweetness[i];
            if (curSum >= n){
                count++;
                curSum = 0;
            }
        }
        return count >= K + 1;
    }
}
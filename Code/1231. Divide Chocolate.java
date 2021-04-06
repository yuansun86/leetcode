class Solution {
    public int maximizeSweetness(int[] sweetness, int K) {
        int left = 0;
        int right = (int)1e9;
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            int partscount = dividedParts(sweetness, mid);
            if (partscount >= K + 1){
                left = mid;
            }else{
                right = mid;
            }
        }
        

        if (dividedParts(sweetness, right) >= K + 1){
            return right;
        }
        if (dividedParts(sweetness, left) >= K + 1){
            return left;
        }
        return 1;
    }
    
    private int dividedParts(int[] sweetness, int minsweet){
        int res = 0;
        int cur = 0;
        for (int sweet: sweetness){
            if (cur + sweet >= minsweet){
                res += 1;
                cur = 0;
            }else{
                cur += sweet;
            }
        }
        return res;
    }
}
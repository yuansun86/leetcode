class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int speed = piles[0];
        for (int i = 0; i<piles.length; i++){
            if (piles[i] > speed){
                speed = piles[i];
            }
        }
        
        int l = 0;
        int r = speed;
        while (l + 1 < r){
            int mid = l + (r - l) / 2;
            if (finishHours(piles, mid) > h){
                l = mid;
            }else{
                r = mid;
            }
        }
        if (finishHours(piles, l) <= h){
            return l;
        }
        if (finishHours(piles, r) <= h){
            return r;
        }
        return 0;
    }
    
    private int finishHours(int[] piles, int speed){
        if (speed == 0){
            return Integer.MAX_VALUE;
        }
        int res = 0;
        for (int i = 0; i < piles.length; i++){
            res += Math.ceil(piles[i] / (speed*1.0));
        }
        return res;
    }
}
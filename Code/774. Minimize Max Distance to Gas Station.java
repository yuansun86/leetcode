class Solution {
    public double minmaxGasDist(int[] stations, int k) {
        double left = 0.0;
        double right = (stations[stations.length - 1] - stations[0]) * 1.0;
        
        while (left + 1e-6 < right){
            double mid = left + (right - left) / 2;
            int stationsNeeded = numOfStation(stations, mid);
            if (stationsNeeded > k){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (numOfStation(stations, left) <= k){
            return left;
        }
        if (numOfStation(stations, right) <= k){
            return right;
        }
        return 0.0;
    }
    
    private int numOfStation(int[] stations, double penalty){
        int res = 0;
        for (int i = 0; i < stations.length - 1; i++){
            int gap = stations[i + 1] - stations[i];
            res += Math.ceil(gap / penalty) - 1;
        }
        return res;
    }
}
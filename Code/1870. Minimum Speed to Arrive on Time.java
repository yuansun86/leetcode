class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        int left = 0;
        int right = (int)1e7;

        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (timeNeeded(dist, mid) <= hour){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        if (timeNeeded(dist, left) <= hour) return left;
        if (timeNeeded(dist, right) <= hour) return right;
        return -1;
        
    }
    
    private double timeNeeded(int[] dist, int speed){
        if (dist.length == 1){
            return dist[0] * 1.0 / speed;
        }
        
        double hours = 0.0;
        for (int i = 0; i < dist.length - 1; i++){
            hours += (int)Math.ceil(dist[i] * 1.0 / speed);
        }
        
        hours += dist[dist.length - 1] * 1.0 / speed;
        return hours;
    }
}
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        Arrays.sort(satisfaction);
        int n = satisfaction.length;
        int res = 0;
        int curSat = 0;
        for (int i = n - 1; i >= 0; i--){
            if (satisfaction[i] + curSat <= 0) return res;
            curSat += satisfaction[i];
            res += curSat;
        }   
        return res;
    }
}
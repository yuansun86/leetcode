class Solution {
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (int[] x, int[] y) -> (y[1] - y[0]) - (x[1] - x[0]));
        int left = 0;
        int right = 0;
        for (int i = 0; i < tasks.length; i++){
            right += tasks[i][1];
        }
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (validNumber(tasks, mid)){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        if (validNumber(tasks, left)) return left;
        if (validNumber(tasks, right)) return right;
        return right;
    }
    
    private boolean validNumber(int[][] tasks, int energy){
        for (int i = 0; i < tasks.length; i++){
            if (energy < tasks[i][1]) return false;
            energy -= tasks[i][0];
        }
        return true;
    }

}
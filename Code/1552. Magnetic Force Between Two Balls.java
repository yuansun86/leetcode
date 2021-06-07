class Solution {
    public int maxDistance(int[] position, int m) {
        int left = 0;
        int right = 0;
        int start = Integer.MIN_VALUE;
        for (int i: position){
            right = Math.max(right, i);
            start = Math.min(start, i);
        }
        right = right / (m - 1);
        
        TreeSet set = new TreeSet();
        for (int i : position){
            set.add(i);
        }
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (validGap(set, start, mid, m)){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (validGap(set, start, right, m)){
            return right;
        }
        if (validGap(set, start, left, m)){
            return left;
        }
        return 0;
    }
    
    private boolean validGap(TreeSet set, int start, int gap, int m){
        int count = 0;
        int cur = start;
        while (count < m){
            if (set.ceiling(cur) == null){
                return false;
            }else{
                cur = (int)set.ceiling(cur) + gap;
                count++;
            }
        }
        return true;
    }
}
class Solution {
    public int hIndex(int[] citations) {
        int length = citations.length;
        int left = 0;
        int right = length - 1;
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (citations[mid] >= length - mid){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        if (citations[left] >= length - left) return length - left;
        if (citations[right] >= length - right) return length - right;
        return 0;
        
    }
}
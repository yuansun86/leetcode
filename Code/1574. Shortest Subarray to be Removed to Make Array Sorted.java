class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int left = 0;
        while (left + 1 < arr.length){
            if (arr[left] <= arr[left + 1]){
                left++;
            }else{
                break;
            }
        }
        if (left == arr.length - 1){
            return 0;
        }
        
        int right = arr.length - 1;
        while (right - 1 >= 0){
            if (arr[right] >= arr[right-1]){
                right--;
            }else{
                break;
            }
        }
        
        int res = Math.min(arr.length - left - 1, right);
        
        int i = 0;
        int j = right;
        while (i <= left && j <= arr.length - 1){
            if (arr[i] <= arr[j]){
                res = Math.min(res, j - i - 1);
                i++;
            }else{
                j++;
            }
        }
        return res;
    }
}
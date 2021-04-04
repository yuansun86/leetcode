class Solution {
    public int maxSum(int[] nums1, int[] nums2) {
        long mod = (long)1e9 + 7;
        long res1 = 0;
        long res2 = 0;
        int i = 0;
        int j = 0;
        while (i < nums1.length || j < nums2.length){
            if (i >= nums1.length){
                res2 = res2 + nums2[j];
                j++;
            }else if (j >= nums2.length){
                res1 = res1 + nums1[i];
                i++;
            }else if (nums1[i] < nums2[j]){
                res1 = res1 + nums1[i];
                i++;
            }else if (nums2[j] < nums1[i]){
                res2 = res2 + nums2[j];
                j++;
            }else{
                res1 = res1 + nums1[i];
                res2 = res2 + nums2[j];
                res1 = Math.max(res1, res2);
                res2 = res1;
                i++;
                j++;
            }
        }
        return (int)(Math.max(res1, res2) % mod);
    }
}
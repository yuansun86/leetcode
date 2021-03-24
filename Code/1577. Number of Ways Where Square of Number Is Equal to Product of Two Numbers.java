class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        return helper(nums1, nums2) + helper(nums2, nums1);
        
    }
    
    public int helper(int[] nums1, int[] nums2){
        Map<Long, Integer> square = new HashMap<>();
        Map<Long, Integer> product = new HashMap<>();
        for (int i = 0; i < nums1.length; i++){
            Long key = (long)nums1[i] * (long)nums1[i];
            if (!square.containsKey(key)){
                square.put(key, 1);
            }else{
                square.put(key, square.get(key) + 1);
            }
        }
        
        for (int i = 0; i < nums2.length; i++){
            for (int j = i + 1; j < nums2.length;j++){
                Long key = (long)nums2[i] * (long)nums2[j];
                if (!product.containsKey(key)){
                    product.put(key, 1);
                }else{
                    product.put(key, product.get(key) + 1);
                }
            }
        }
        
        int res = 0;
        for (Long i: square.keySet()){
            if (product.containsKey(i)){
                res += square.get(i) * product.get(i);
            }
        }
        return res;
    }
}
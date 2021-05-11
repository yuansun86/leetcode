class Solution {
    public int oddEvenJumps(int[] arr) {
        if (arr.length <= 1) return arr.length;
        int length = arr.length;
        
        boolean[] odd = new boolean[arr.length];
        boolean[] even = new boolean[arr.length];
        odd[arr.length - 1] = true;
        even[arr.length - 1] = true;
        int res = 1;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        map.put(arr[length - 1], length - 1);
        
        for (int i = length - 2; i >= 0; i--){
            Integer nextGreater = map.ceilingKey(arr[i]);
            if (nextGreater != null){
                odd[i] = even[map.get(nextGreater)];
            }
            
            Integer nextSmaller = map.floorKey(arr[i]);
            if (nextSmaller != null){
                even[i] = odd[map.get(nextSmaller)];
            }
            
            if (odd[i] == true) res++;
            
            map.put(arr[i], i);

        }
        return res;
    }
}
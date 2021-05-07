class Solution {
    public int maxJumps(int[] arr, int d) {
        TreeMap<Integer, List<Integer>> indexes = new TreeMap<>();
        for (int i = 0; i < arr.length; i++){
            int val = arr[i];
            List<Integer> entry = indexes.containsKey(val)?indexes.get(val):new ArrayList<>();
            entry.add(i);
            indexes.put(val, entry);
        }
        
        Iterator<Integer> iter = indexes.keySet().iterator();
        int[] dp = new int[arr.length];
        while (iter.hasNext()){
            Integer val = iter.next();
            for (int index : indexes.get(val)){
                checkDP(arr, dp, d, index);   
            }
        }

        int res = 0;
        for (int i : dp){
            res = Math.max(res, i);
        }
        return res;
    }
    
    private void checkDP(int[] arr, int[] dp, int d, int index){
        dp[index] = 1;
        for (int i = index + 1; i <= index + d; i++){
            if (i >= dp.length || arr[i] >= arr[index])
                break;
            dp[index] = Math.max(dp[index], dp[i] + 1);
        }
        
        for (int i = index - 1; i >= index - d; i--){
            if (i < 0 || arr[i] >= arr[index])
                break;
            dp[index] = Math.max(dp[index], dp[i] + 1);
        }
    }
}
class Solution {
    int result = 0;
    public int pathSum(int[] nums) {
        Map<Integer, Integer> values = new HashMap();
        for (int num: nums){
            values.put(num / 10, num % 10);
        }
        dfs(nums[0]/10, 0, values);
        return result;
    }
    
    private void dfs(int node, int sum, Map<Integer, Integer> values){
        if (!values.containsKey(node))return;
        
        sum += values.get(node);
        int depth = node / 10;
        int pos = node % 10;
        int left = (depth + 1) * 10 + 2 * pos - 1;
        int right = (depth + 1) * 10 + 2 * pos;
        
        if (!values.containsKey(left) && !values.containsKey(right)){
            result += sum;
        }else{
            dfs(left, sum, values);
            dfs(right, sum, values);
        }
    }
    

}
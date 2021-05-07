class Solution {
    public boolean canReach(int[] arr, int start) {
        Deque<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet();
        queue.offerLast(start);
        visited.add(start);
        while(queue.size() > 0){
            int loopTimes = queue.size();
            for (int i = 0; i < loopTimes; i++){
                Integer index = queue.pollFirst();
                if (arr[index] == 0){
                    return true;
                }
                int left = index - arr[index];
                if (left >= 0 && !visited.contains(left)){
                    queue.offerLast(left);
                    visited.add(left);
                }
                
                int right = index + arr[index];
                if (right < arr.length && !visited.contains(right)){
                    queue.offerLast(right);
                    visited.add(right);
                }
            }
        }
        
        return false;
    }
}
class Solution {
    public int minJumps(int[] arr) {
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        Map<Integer, List<Integer>> valToIndex = new HashMap();
        
        for (int i = 0; i < arr.length; i++){
            if (valToIndex.containsKey(arr[i])){
                valToIndex.get(arr[i]).add(i);
            }else{
                List<Integer> entry = new ArrayList<>();
                entry.add(i);
                valToIndex.put(arr[i], entry);
            }
        }
        
        queue.offer(0);
        visited.add(0);
        int steps = -1;
        while (!queue.isEmpty()){
            int loops = queue.size();
            steps++;
            for (int i = 0; i < loops; i++){
                int index = queue.poll();
                if (index == arr.length - 1){
                    return steps;
                }
                
                if (index - 1 >=0 && !visited.contains(index - 1)){
                    queue.offer(index - 1);
                    visited.add(index - 1);
                }
                
                if (index + 1 < arr.length && !visited.contains(index + 1)){
                    queue.offer(index + 1);
                    visited.add(index + 1);
                }
                
                for (Integer sameVal : valToIndex.get(arr[index])){
                    if (!visited.contains(sameVal)){
                        queue.offer(sameVal);
                        visited.add(sameVal);
                    }
                }
                valToIndex.get(arr[index]).clear();
            }
        }
        return 0;
    }
}
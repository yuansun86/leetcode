class RandomizedCollection {
    private List<Integer> nums;
    private Map<Integer, List<Integer>> map;
    private Random random;
    
    /** Initialize your data structure here. */
    public RandomizedCollection() {
        nums = new ArrayList();
        map = new HashMap();
        random = new Random();
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val)){
            List<Integer> entry = map.get(val);
            entry.add(nums.size());
            nums.add(val);
            return false;
        }
        
        List<Integer> entry = new ArrayList();
        entry.add(nums.size());
        nums.add(val);
        map.put(val, entry);
        return true;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val)){
            return false;
        }
        
        List<Integer> entry = map.get(val);
        int removeIndex = entry.get(entry.size() - 1);
        if (removeIndex == nums.size() - 1){
            entry.remove(entry.size() - 1);
            nums.remove(nums.size() - 1);
            if (entry.size() == 0){
                map.remove(val);
            }
            return true;   
        }
        entry.remove(entry.size() - 1);
        if (entry.size() == 0){
            map.remove(val);
        }
        
        int lastVal = nums.get(nums.size() - 1);
        int lastValOriginalIndex = nums.size() - 1;
        nums.set(removeIndex, lastVal);
        nums.remove(nums.size() - 1);
        List<Integer> lastValEntry = map.get(lastVal);
        lastValEntry.remove(Integer.valueOf(lastValOriginalIndex));
        lastValEntry.add(removeIndex);

        return true;
    }
    
    /** Get a random element from the collection. */
    public int getRandom() {
        int randomIndex = random.nextInt(nums.size());
        return nums.get(randomIndex);
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
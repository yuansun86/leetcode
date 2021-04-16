class RandomizedSet {
    private Set<Integer> set;
    private List<Integer> list;
    private Random random;
    
    
    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.set = new HashSet();
        this.list = new ArrayList();
        this.random = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (set.contains(val)){
            return false;
        }
        set.add(val);
        list.add(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!set.contains(val)){
            return false;
        }
        
        int index = list.indexOf(val);
        list.set(index, list.get(list.size() - 1));
        list.remove(list.size() - 1);
        set.remove(val);
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        int randomIndex = random.nextInt(list.size());
        return list.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
class AllOne {
    private Bag head;
    private Bag tail;
    private Map<Integer, Bag> countToBag;
    private Map<String, Integer> stringToCount;
    
    
    private class Bag{
        int count;
        Set<String> contents;
        Bag next;
        Bag prev;
        
        public Bag(int cnt){
            count = cnt;
            contents = new HashSet();
        }
        
        public void add(String key){
            contents.add(key);
        }
        
        public void remove(String key){
            contents.remove(key);
        }
    }
    
    /** Initialize your data structure here. */
    public AllOne() {
        head = new Bag(Integer.MIN_VALUE);
        tail = new Bag(Integer.MAX_VALUE);
        head.next = tail;
        tail.prev = head;
        countToBag = new HashMap();
        stringToCount = new HashMap();
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        if (!stringToCount.containsKey(key)){
            stringToCount.put(key, 1);
            Bag oneBag;
            if (countToBag.containsKey(1)){
                oneBag = countToBag.get(1);
            }else{
                //initialize oneBag and place it behind head.
                oneBag = new Bag(1);
                countToBag.put(1, oneBag);
                Bag afterHead = head.next;
                head.next = oneBag;
                oneBag.prev = head;
                oneBag.next = afterHead;
                afterHead.prev = oneBag;
            }
            oneBag.add(key);
        }else{
            //find original bag, remove it from original bag, place it into next bag;
            int originalCount = stringToCount.get(key);
            int newCount = originalCount + 1;
            stringToCount.put(key, newCount);
            Bag originalBag = countToBag.get(originalCount);
            originalBag.remove(key);
            Bag newBag;
            if (countToBag.containsKey(newCount)){
                newBag = countToBag.get(newCount);
            }else{
                newBag = new Bag(newCount);
                countToBag.put(newCount, newBag);
                Bag afterPrev = originalBag.next;
                originalBag.next = newBag;
                newBag.prev = originalBag;
                newBag.next = afterPrev;
                afterPrev.prev = newBag;
            }
            newBag.add(key);
            
            // check if need to delete original bag
            if (originalBag.contents.isEmpty()){
                Bag beforeOriginal = originalBag.prev;
                Bag afterOriginal = originalBag.next;
                beforeOriginal.next = afterOriginal;
                afterOriginal.prev = beforeOriginal;
                countToBag.remove(originalCount);
        }
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        //find original bag, remove it from original bag, place it into prev bag;
        int originalCount = stringToCount.get(key);
        Bag originalBag = countToBag.get(originalCount);
        int newCount = originalCount - 1;
        originalBag.remove(key);
        Bag newBag;
        if (newCount == 0){
            // update information
            stringToCount.remove(key);
        }else{
            // add it into newBag, update information
            if (countToBag.containsKey(newCount)){
                newBag = countToBag.get(newCount);
            }else{
                newBag = new Bag(newCount);
                countToBag.put(newCount, newBag);
                Bag beforeOriginal = originalBag.prev;
                beforeOriginal.next = newBag;
                newBag.prev = beforeOriginal;
                newBag.next = originalBag;
                originalBag.prev = newBag;
            }
            newBag.add(key);
            stringToCount.put(key, newCount);
        }
        
        // check if need to delete original bag
        if (originalBag.contents.isEmpty()){
            Bag beforeOriginal = originalBag.prev;
            Bag afterOriginal = originalBag.next;
            beforeOriginal.next = afterOriginal;
            afterOriginal.prev = beforeOriginal;
            countToBag.remove(originalCount);
        }
    }
    
    /** Returns one of the keys with maximal value. */
    public String getMaxKey() {
        Bag maxBag = tail.prev;
        if (maxBag.contents.isEmpty()){
            return "";
        }else{
            return maxBag.contents.iterator().next();
        }
    }
    
    /** Returns one of the keys with Minimal value. */
    public String getMinKey() {
        Bag minBag = head.next;
        if (minBag.contents.isEmpty()){
            return "";
        }else{
            return minBag.contents.iterator().next();
        }        
    }
    
}



/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
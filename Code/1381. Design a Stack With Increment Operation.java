class CustomStack {
    private int maxSize;
    private Deque<Integer[]> deque;
    private int size;
    
    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        deque = new LinkedList<>();
        this.size = 0;
    }
    
    public void push(int x) {
        if (this.size >= this.maxSize){
            return;
        }
        Integer[] entry = new Integer[1];
        entry[0] = x;
        deque.offerLast(entry);
        this.size++;
    }
    
    public int pop() {
        if (this.size == 0){
            return -1;
        }
        
        this.size--;
        return deque.pollLast()[0];
        
    }
    
    public void increment(int k, int val) {
        Iterator<Integer[]> iter = deque.iterator();
        while (k > 0 && iter.hasNext()){
            Integer[] entry = iter.next();
            entry[0] += val;
            k--;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
class LFUCache {
    class Node{
        int key, value, count;
        Node next, prev;
        
        Node(int key, int value){
            this.key = key;
            this.value = value;
            this.count = 1;
        }  
    }
    
    class DLList{
        Node head, tail;
        int size;
        DLList(){
            head = new Node(0, 0);
            tail = new Node(0, 0);
            head.next = tail;
            tail.prev = head;
        }
        
        void add(Node node){
            head.next.prev = node;
            node.prev = head;
            node.next = head.next;
            head.next = node;
            size++;
        }
        
        void remove(Node node){
            node.prev.next = node.next;
            node.next.prev = node.prev;
            size--;
        }
        
        Node popLast(){
            if (size <= 0){
                return null;
            }
            
            Node res = tail.prev;
            remove(res);
            return res;
        }
    }    

    int capacity;
    int size;
    int curMinCount;
    Map<Integer, Node> nodeMap;
    Map<Integer, DLList> countMap;
    
    
    
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.curMinCount = 0;
        this.nodeMap = new HashMap();
        this.countMap = new HashMap();
    }
    
    public int get(int key) {
        Node node = nodeMap.get(key);
        if (node == null) return -1;
        update(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (this.capacity == 0) return;
        Node node;
        if (nodeMap.containsKey(key)){
            node = nodeMap.get(key);
            node.value = value;
            update(node);
            return;
        }
        
        node = new Node(key, value);
        nodeMap.put(key, node);
        if (this.size == this.capacity){
            DLList minList = countMap.get(this.curMinCount);
            Node removeNode = minList.popLast();
            nodeMap.remove(removeNode.key);
            this.size--;
        }
        
        this.size++;
        this.curMinCount = 1;
        DLList newList = countMap.getOrDefault(1, new DLList());
        newList.add(node);
        countMap.put(1, newList);
    }
    
    private void update(Node node){
        int currCount = node.count;
        DLList currDLList = countMap.get(currCount);
        currDLList.remove(node);
        if (currDLList.size == 0 && currCount == this.curMinCount){
            this.curMinCount++;
        }
        node.count++;
        DLList newDLList = countMap.getOrDefault(node.count, new DLList());
        newDLList.add(node);
        countMap.put(node.count, newDLList);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
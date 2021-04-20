class LRUCache {
    private int capacity;
    private int size;
    private Node head;
    private Node tail;
    private Map<Integer, Node> keyToPrev;
    
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.head = new Node(-1, -1);
        this.tail = this.head;
        this.keyToPrev = new HashMap();
    }
    
    public int get(int key) {
        if (!keyToPrev.containsKey(key)){
            return -1;
        }
        
        // get the node (prev.next), move the node to the front, and return the value;
        Node prev = keyToPrev.get(key);
        Node curr = prev.next;
        if (prev == head){
            return curr.val;
        }
        prev.next = curr.next;
        
        if (curr == tail){
            tail = prev;
        }else{
            keyToPrev.put(prev.next.key, prev);
        }
        
        curr.next = head.next;
        head.next = curr;
        keyToPrev.put(curr.key, head);
        if (curr.next != null){
            keyToPrev.put(curr.next.key, curr);
        }
        return curr.val;
    }
    
    public void put(int key, int value) {
        if (keyToPrev.containsKey(key)){
            get(key);
            Node curr = keyToPrev.get(key).next;
            curr.val = value;
            return;
        }
        
        Node newNode = new Node(key, value);
        newNode.next = head.next;
        head.next = newNode;
        if (newNode.next != null){
            keyToPrev.put(newNode.next.key, newNode);
        }else{
            tail = newNode;
        }
        keyToPrev.put(newNode.key, head);
        this.size++;
        
        if (this.size > this.capacity){
            Node newTail = keyToPrev.get(tail.key);
            int oldTailKey = tail.key;
            newTail.next = null;
            keyToPrev.remove(oldTailKey);
            tail = newTail;
            this.size--;
        }

    }
}

class Node{
    public int key;
    public int val;
    public Node next;
    
    Node(int key, int val){
        this.key = key;
        this.val = val;
        this.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
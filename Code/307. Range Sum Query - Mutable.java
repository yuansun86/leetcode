class NumArray {
    class Node{
        int start;
        int end;
        int sum;
        Node left;
        Node right;
        
        Node(int start, int end, int sum){
            this.start = start;
            this.end = end;
            this.sum = sum;
        }
    }
    
    private Node buildSegmentTree(int start, int end, int[] nums){
        if (start == end){
            return new Node(start, end, nums[start]);
        }
        
        int mid = start + (end - start) / 2;
        Node left = buildSegmentTree(start, mid, nums);
        Node right = buildSegmentTree(mid + 1, end, nums);
        Node res = new Node(start, end, left.sum + right.sum);
        res.left = left;
        res.right = right;
        return res;
    }
    
    private void updateTree(Node root, int index, int val){
        if (root.start == root.end && root.start == index){
            root.sum = val;
            return;   
        }
        
        int mid = root.start + (root.end - root.start) / 2;
        if (index <= mid){
            updateTree(root.left, index, val);
        }else{
            updateTree(root.right, index, val);
        }
        root.sum = root.left.sum + root.right.sum;
    }
    
    
    private int querySum(Node root, int left, int right){
        if (root.start == left && root.end == right){
            return root.sum;
        }
        
        int mid = root.start + (root.end - root.start) / 2;
        if (right <= mid){
            return querySum(root.left, left, right);
        }else if (left > mid){
            return querySum(root.right, left, right);
        }else{
            return querySum(root.left, left, mid) + querySum(root.right, mid + 1, right);
        }
    }
    
    Node rootNode;
    
    public NumArray(int[] nums) {
        rootNode = this.buildSegmentTree(0, nums.length - 1, nums);
    }
    
    public void update(int index, int val) {
        this.updateTree(rootNode, index, val);
    }
    
    public int sumRange(int left, int right) {
        return this.querySum(rootNode, left, right);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
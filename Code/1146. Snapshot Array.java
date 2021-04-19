class SnapshotArray {
    private int snapId;
    TreeMap<Integer, Integer>[] data;
    
    public SnapshotArray(int length) {
        data = new TreeMap[length];
        snapId = 0;
        for (int i = 0; i < length; i++){
            data[i] = new TreeMap<Integer, Integer>();
            data[i].put(0, 0);
        }
    }
    
    public void set(int index, int val) {
        TreeMap<Integer, Integer> entry = data[index];
        entry.put(snapId, val);
    }
    
    public int snap() {
        return snapId++;
    }
    
    public int get(int index, int snap_id) {
        TreeMap<Integer, Integer> entry = data[index];
        return entry.floorEntry(snap_id).getValue();
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
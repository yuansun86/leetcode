class Solution {
    class Item{
        int index;
        int value;
        int count;
        
        Item(int index, int value){
            this.index = index;
            this.value = value;
            this.count = 0;
        }
    }
    
    public List<Integer> countSmaller(int[] nums) {
        Item[] toSort = new Item[nums.length];
        for (int i = 0; i < toSort.length; i++){
            toSort[i] = new Item(i, nums[i]);
        }
        mergeSort(toSort, 0, toSort.length - 1);
        int[] res = new int[nums.length];
        for (Item item:toSort){
            int index = item.index;
            int count = item.count;
            res[index] = count;
        }
        
        List<Integer> result = new ArrayList<>();
        for (int i: res){
            result.add(i);
        }
        return result;
    }
    
    private void mergeSort(Item[] items, int start, int end){
        if (start >= end){
            return;
        }
        
        int mid = start + (end - start) / 2;
        mergeSort(items, start, mid);
        mergeSort(items, mid + 1, end);
        
        int rightcount = 0;
        List<Item> temp = new ArrayList<>();
        int i = start;
        int j = mid + 1;
        while (i <= mid && j <= end){
            if (items[i].value <= items[j].value){
                temp.add(items[i]);
                items[i].count += rightcount;
                i++;
            }else{
                temp.add(items[j]);
                rightcount++;
                j++;
            }
        }
        while (i <= mid){
            temp.add(items[i]);
            items[i].count += rightcount;
            i++;
        }
        while (j <= end){
            temp.add(items[j]);
            rightcount++;
            j++;
        }
        
        for (int k = start; k <= end; k++){
            items[k] = temp.get(k - start);
        }
    }
}
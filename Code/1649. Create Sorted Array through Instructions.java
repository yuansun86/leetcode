class Solution {
    int MOD = (int)1e9 + 7;
    class Item{
            int index;
            int value;
            int smaller;
            int larger;

            Item(int index, int value){
                this.index = index;
                this.value = value;
                this.smaller = 0;
                this.larger = 0;
            }
        }

    private int count(int[] nums) {
        Item[] toSort = new Item[nums.length];
        for (int i = 0; i < toSort.length; i++){
            toSort[i] = new Item(i, nums[i]);
        }
        mergeSort(toSort, 0, toSort.length - 1);
        int[] res = new int[nums.length];
        for (Item item:toSort){
            int index = item.index;
            int smaller = item.smaller;
            int larger = item.larger;
            res[index] = Math.min(smaller, larger);
        }
        int result = 0;
        for (int val: res){
            result = (result + val)%MOD;
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

        int i = start;
        for (int j = mid + 1; j <= end; j++){
            while (i <= mid && items[i].value < items[j].value){
                i++;
            }
            items[j].smaller += (i - start);
        }
        
        i = start;
        for (int j = mid + 1; j <= end; j++){
            while (i <= mid && items[i].value <= items[j].value){
                i++;
            }
            items[j].larger += (mid - i + 1);
        }

        List<Item> temp = new ArrayList<>();
        int left = start, right = mid + 1;
        while (left <= mid && right <= end){
            if (items[left].value <= items[right].value){
                temp.add(items[left++]);
            }else{
                temp.add(items[right++]);
            }
        }
        
        while (left <= mid){
            temp.add(items[left++]);
        }
        while (right <= end){
            temp.add(items[right++]);
        }        
        
        for (int k = start; k <= end; k++){
            items[k] = temp.get(k - start);
        }
    }
    
    public int createSortedArray(int[] instructions) {
        return count(instructions);
    }
}
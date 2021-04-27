class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] prefix = new long[nums.length + 1];
        for (int i = 1; i < prefix.length; i++){
            prefix[i] = prefix[i - 1] + nums[i -1];
        }
        return mergeAndCount(prefix, 0, prefix.length - 1, lower, upper);
        
    }
    
    private int mergeAndCount(long[] prefix, int start, int end, int lower, int upper){
        if (start >= end){
            return 0;
        }
        
        int mid = start + (end - start) / 2;
        int count = mergeAndCount(prefix, start, mid, lower, upper) + mergeAndCount(prefix, mid + 1, end, lower, upper);
        for (int i = start; i <= mid; i++){
            int leftBound = mid + 1, rightBound = end;
            while (leftBound <= end && prefix[leftBound] - prefix[i] < lower){
                leftBound++;
            }
            
            while (rightBound >= mid + 1 && prefix[rightBound] - prefix[i] > upper){
                rightBound--;
            }
            if (rightBound >= leftBound){
                count += (rightBound - leftBound + 1);
            }
        }
        List<Long> temp = new ArrayList<>();
        int left = start, right = mid + 1;
        while(left <= mid && right <= end){
            if (prefix[left] <= prefix[right]){
                temp.add(prefix[left]);
                left++;
            }else{
                temp.add(prefix[right]);
                right++;
            }
        }
        while(left <= mid){
            temp.add(prefix[left]);
            left++;
        }
        while(right <= end){
            temp.add(prefix[right]);
            right++;
        }
        
        int offset = 0;
        for (int j = 0; j < temp.size();j++){
            prefix[start + offset] = temp.get(j);
            offset++;
        }
        
        return count;
    }
}
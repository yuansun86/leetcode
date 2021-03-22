class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        if (slots1 == null || slots2 == null){
            return new ArrayList<Integer>();
        }
        Arrays.sort(slots1,  (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(slots2,  (a, b) -> Integer.compare(a[0], b[0]));
        
        int i = 0;
        int j = 0;
        Integer[] resArray = new Integer[2];
        while (i < slots1.length && j < slots2.length){
            int[] left = slots1[i];
            int[] right = slots2[j];
            if (left[0] >= right[1]){
                j++;
                continue;
            }else if (right[0] >= left[1]){
                i++;
                continue;
            }
            

            if (Math.min(left[1], right[1]) - Math.max(left[0], right[0]) >= duration){
                resArray[0] = Math.max(left[0], right[0]);
                resArray[1] = resArray[0] + duration;
                return new ArrayList<Integer>(Arrays.asList(resArray));
            }else{
                if(left[1] >= right[1]){
                    j++;
                }else{
                    i++;
                }
            }
        }
        return new ArrayList<Integer>();
    }
}
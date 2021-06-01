class Solution {
    public int minInsertions(String s) {
        int res = 0;
        int right = 0;
        for (char c : s.toCharArray()){
            if (c == ')'){
                right--;
                if (right < 0){
                    res++;
                    right += 2;
                }
            }else{
                if (right % 2 == 0){
                    right += 2;
                }else{
                    res++;
                    right--;
                    right += 2;
                }
            }
        }
        return res + right;
    }
}
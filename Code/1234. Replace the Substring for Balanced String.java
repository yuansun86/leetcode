class Solution {
    public int balancedString(String s) {
        int[] count = new int[4];
        for (char c: s.toCharArray()){
            count[getIndex(c)] += 1;
        }
        int n = s.length();
        int res = n;
        int balanceNum = n / 4;
        for (int i = 0; i < 4; i++){
            if (count[i] > balanceNum){
                count[i] = count[i] - balanceNum;
            }else{
                count[i] = 0;
            }
        }
        
        int j = 0;
        int[] cur = new int[4];
        if (match(cur, count)){
            return 0;
        }
        for (int i = 0; i < s.length(); i++){
            while (j < s.length() && !match(cur, count)){
                cur[getIndex(s.charAt(j))] += 1;
                j++;
            }
            
            if (match(cur, count)){
                res = Math.min(res, j - i);
            }
            cur[getIndex(s.charAt(i))] -= 1;
        }

        return res;
    }
    
    private boolean match(int[] cur, int[] count){
        for (int i = 0; i < 4; i++){
            if (count[i] == 0 || cur[i] >= count[i]){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
    
    private int getIndex(char c){
        if (c == 'Q'){
            return 0;
        }else if (c == 'W'){
            return 1;
        }else if (c == 'E'){
            return 2;
        }else if (c == 'R'){
            return 3;
        }
        return 0;
    }
}
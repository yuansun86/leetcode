class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int[] leftBound = new int[26];
        int[] rightBound = new int[26];
        Arrays.fill(leftBound, s.length());
        for (int i = 0; i < s.length(); i++){
            int ch = s.charAt(i) - 'a';
            leftBound[ch] = Math.min(leftBound[ch], i);
            rightBound[ch] = i;
        }
        
        List<String> res = new ArrayList<>();
        int right = -1;
        for (int i = 0; i < s.length(); i++){
            if (i == leftBound[s.charAt(i) - 'a']){
                int newRight = checkRight(s, i, leftBound, rightBound);
                if (newRight == -1) {
                    continue;
                }else{
                    if (i > right) res.add("");
                    right = newRight;
                    res.set(res.size() - 1, s.substring(i, right + 1));
                }
            }
        }
        return res;
    }
    
    public int checkRight(String s, int i, int[] leftBound, int[] rightBound){
        int right = rightBound[s.charAt(i) - 'a'];
        for (int j = i; j <= right; j++){
            if (leftBound[s.charAt(j) - 'a'] < i) return -1;
            right = Math.max(right, rightBound[s.charAt(j) - 'a']);
        }
        return right;
    }
}
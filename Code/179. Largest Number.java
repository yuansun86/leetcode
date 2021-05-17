class Solution {
    public String largestNumber(int[] nums) {
        String[] a = new String[nums.length];
        for (int i = 0; i < nums.length; i++){
            a[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(a, new CustomComparator());
        StringBuilder sb = new StringBuilder();
        for (String x: a){
            sb.append(x);
        }
        String res = sb.toString();
        if (res.charAt(0) == '0'){
            return "0";
        }
        return res;
    }
    
    public class CustomComparator implements Comparator<String>{
        @Override
        public int compare(String a, String b){
            String A = a + b;
            String B = b + a;
            return B.compareTo(A);
        }
    } 
}

// class Solution {
//     public String largestNumber(int[] nums) {
//         Integer[] a = new Integer[nums.length];
//         for (int i = 0; i < nums.length; i++){
//             a[i] = nums[i];
//         }
//         Arrays.sort(a, new CustomComparator());
//         StringBuilder sb = new StringBuilder();
//         for (Integer x: a){
//             sb.append(x);
//         }
//         String res = sb.toString();
//         if (res.charAt(0) == '0'){
//             return "0";
//         }
//         return res;
//     }
    
//     public class CustomComparator implements Comparator<Integer>{
//         public int compare(Integer A, Integer B){
//             String a = A.toString();
//             String b = B.toString();
//             int i = 0;
//             while (i < a.length() && i < b.length()){
//                 int x = (int)a.charAt(i);
//                 int y = (int)b.charAt(i);
//                 if (x > y){
//                     return -1;
//                 }else if (x < y){
//                     return 1;
//                 }
//                 i++;
//             }
            
//             if (i == a.length() && i == b.length()){
//                 return 0;
//             }else{
//                 Long m = Long.parseLong(a + b);
//                 Long n = Long.parseLong(b + a);
//                 return m > n?-1:1;
//             }
//         }
//     } 
// }

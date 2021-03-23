class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        List<Integer> unhappy = new ArrayList<>();
        int sat = 0;
        for (int i = 0; i < customers.length; i++){
            if (grumpy[i] == 0){
                sat += customers[i];
                unhappy.add(0);
            }else{
                unhappy.add(customers[i]);
            }
        }
        int[] prefix = new int[customers.length + 1];
        for (int i = 1; i < prefix.length; i++){
             prefix[i] = prefix[i - 1] + unhappy.get(i - 1);
        }
        int flip = 0;
        for (int i = 0; i < prefix.length - X; i++){
            flip = Math.max(flip, prefix[i + X] - prefix[i]);
        }
        return sat + flip;

    }
}
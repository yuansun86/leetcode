class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < expression.length(); i++){
            Character ch = expression.charAt(i);
            if (ch == '+' || ch == '-' || ch == '*'){
                String left = expression.substring(0, i);
                String right = expression.substring(i + 1, expression.length());
                List<Integer> leftResult = diffWaysToCompute(left);
                List<Integer> rightResult = diffWaysToCompute(right);
                for (Integer leftInteger: leftResult){
                    for (Integer rightInteger: rightResult){
                        if (ch == '+'){
                            res.add(leftInteger + rightInteger);
                        }else if (ch == '-'){
                            res.add(leftInteger - rightInteger);
                        }else if (ch == '*'){
                            res.add(leftInteger * rightInteger);
                        }
                    }
                }
            }
        }
        if (res.isEmpty()){
            res.add(Integer.parseInt(expression));
        }
        return res;
    }
}
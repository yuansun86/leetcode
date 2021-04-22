class NumMatrix {
    private int rows;
    private int cols;
    private int[][] bit;
    
    private int lsb(int n){
        // the right most non-zero bit of a number
        return n & (-n);
    }
    
    private void updateBIT(int r, int c, int val){
        for (int i = r; i <= rows; i += lsb(i)){
            for (int j = c; j <= cols; j += lsb(j)){
                bit[i][j] += val;
            }
        }
    }
    
    
    private int queryBIT(int r, int c){
        int res = 0;
        for (int i = r; i > 0; i -= lsb(i)){
            for (int j = c; j > 0; j -= lsb(j)){
                res += bit[i][j];
            }
        }
        return res;
    }
    
    
    private void buildBIT(int[][] matrix){
        for (int i = 1; i <= rows; i++){
            for (int j = 1; j <= cols; j++){
                int val = matrix[i-1][j-1];
                updateBIT(i, j, val);
            }
        }
    }
    
    public NumMatrix(int[][] matrix) {
        this.rows = matrix.length;
        if (rows == 0)return;
        this.cols = matrix[0].length;
        bit = new int[rows + 1][cols + 1];
        buildBIT(matrix);
    }
    
    public void update(int row, int col, int val) {
        int old_val = sumRegion(row, col, row, col);
        row++;
        col++;
        int diff = val - old_val;
        updateBIT(row, col, diff);
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1++; col1++;row2++;col2++;
        int a = queryBIT(row2, col2);
        int b = queryBIT(row1 - 1, col1 - 1);
        int c = queryBIT(row2, col1 - 1);
        int d = queryBIT(row1 - 1, col2);
        return a + b - c - d;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
Let dp[i][j] = length of the square edge where point matrix[i][j] was used as the bottomright point.
Therefore, in order to construct larger square, we can check dp[i-1][j], dp[i][j-1], dp[i-1][j-1], and get the minimal value. then dp[i][j] = minimal value +1 if matrix[i][j] == '1'

Solution 1, first transpose the matrix, then reverse each row, do it in place
Solution 2, to be implemeted, for each nums[i,j] --> nums[j, n-1-i] --> nums[n-1-i, n-1-j] --> nums[n-1-j, i] --> nums[i, j]. So we can rotate every sublist in iterative way.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result = None
        self.backtracking(board, 0)
    
    def backtracking(self, grid, index):
        if index == 81:
            return True
        x = index // 9
        y = index % 9
        solved = False
        if grid[x][y] != '.':
            solved = self.backtracking(grid, index + 1)
        else:
            validNumbers = self.getValidNumbers(grid, x, y)
            if len(validNumbers) == 0:
                return
            for number in validNumbers:
                grid[x][y] = number
                path.append(grid[x][y])
                solved = self.backtracking(grid, index + 1)
                if solved:
                    break
                path.pop()
                grid[x][y] = '.'
        return solved
                    
    
    
    def getValidNumbers(self, grid, x, y):
        used = set()
        for i in range(9):
            if grid[x][i] != '.':
                used.add(grid[x][i])
            if grid[i][y] != '.':
                used.add(grid[i][y])
        cornerx = 3 * (x // 3)
        cornery = 3 * (y // 3)
        for i in range(3):
            for j in range(3):
                newx = cornerx + i
                newy = cornery + j 
                if grid[newx][newy] != '.':
                    used.add(grid[newx][newy])
        numset = set()
        for i in range(1, 10):
            numset.add(str(i))
        return numset - used
    
    
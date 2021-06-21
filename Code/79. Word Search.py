class Solution:
    res = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, word, i, j)
                if self.res == True:
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        if self.res == True:
            return
        if word == "":
            self.res = True
            return
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == '.':
            return
        if board[i][j] != word[0]:
            return
        letter = board[i][j]
        board[i][j] = "."
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(board, word[1:], i + dx, j + dy)
        board[i][j] = letter
        
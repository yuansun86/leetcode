class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = collections.deque([1])
        dist = {1:0}
        while queue:
            k = queue.popleft()
            if k == n * n:
                return dist[k]
            for i in range(k + 1, min(k + 6, n*n) + 1, 1):
                new_x, new_y = self.convertToCord(i, n)
                if board[new_x][new_y] != -1:
                    i = board[new_x][new_y]
                if i not in dist:
                    queue.append(i)
                    dist[i] = dist[k] + 1
        return -1
    
    def convertToCord(self, k, n):
        k = n * n - k
        if n % 2 == 0:
            i = k // n
            if i % 2 == 0:
                j =  k % n
            else:
                j = n - 1 - k % n
            return i, j
        else:
            i = k // n
            if i % 2 == 0:
                j = n - 1 - k % n
            else:
                j = k % n
            return i, j
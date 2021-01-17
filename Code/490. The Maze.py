class Solution:
    # BFS
    def getNextStop(self, x, y, direction, maze):
        dx, dy = direction
        row, col = len(maze), len(maze[0])
        while True:
            if x + dx < 0 or y + dy < 0:
                return x, y
            if x + dx >= row or y + dy >= col:
                return x, y
            if maze[x + dx][y + dy] == 1:
                return x ,y
            x = x + dx
            y = y + dy
            
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination:
            return True
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add((start[0], start[1]))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for direction in directions:
                newx, newy = self.getNextStop(x, y, direction, maze)
                if (newx, newy) in visited:
                    continue
                if [newx, newy] == destination:
                    return True
                else:
                    queue.append((newx, newy))
                    visited.add((newx, newy))
        return False


class Solution:
    # DFS
    def getNextStop(self, x, y, direction, maze):
        dx, dy = direction
        row, col = len(maze), len(maze[0])
        while True:
            if x + dx < 0 or y + dy < 0:
                return x, y
            if x + dx >= row or y + dy >= col:
                return x, y
            if maze[x + dx][y + dy] == 1:
                return x ,y
            x = x + dx
            y = y + dy
    
    def dfs(self, maze, x, y, visited, destination):
        if [x, y] == destination:
            return True
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            newx, newy = self.getNextStop(x, y, direction, maze)
            if (newx, newy) in visited:
                continue
            visited.add((newx, newy))
            res = self.dfs(maze, newx, newy, visited, destination)
            if res:
                return True
        return False

    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination:
            return True
        visited = set()
        visited.add((start[0], start[1]))
        return self.dfs(maze, start[0], start[1], visited, destination)
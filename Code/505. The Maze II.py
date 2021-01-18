class Solution:
    def getNextStop(self, x, y, dist, direction, maze):
        dx, dy = direction
        row, col = len(maze), len(maze[0])
        new_dist = dist 
        while True:
            if x + dx < 0 or y + dy < 0:
                return x, y, new_dist
            if x + dx >= row or y + dy >= col:
                return x, y, new_dist
            if maze[x + dx][y + dy] == 1:
                return x ,y, new_dist
            x = x + dx
            y = y + dy
            new_dist += 1

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = collections.deque()
        queue.append(start)
        visited = {}
        visited[(start[0], start[1])] = 0
        while queue:
            x, y = queue.popleft()
            dist = visited[(x, y)]
            for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newx, newy, newdist = self.getNextStop(x, y, dist, direction, maze)
                if (newx, newy) in visited:
                    if newdist < visited[(newx, newy)]:
                        visited[(newx, newy)] = newdist
                        queue.append([newx, newy])
                    else:
                        continue
                else:
                    queue.append([newx, newy])
                    visited[(newx, newy)] = newdist
        if (destination[0], destination[1]) in visited:
            return visited[(destination[0], destination[1])]
        else:
            return -1
                
                
        
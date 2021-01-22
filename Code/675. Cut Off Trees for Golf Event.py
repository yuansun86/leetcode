
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        heights = []
        m = len(forest)
        n = len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    heights.append([forest[i][j], i, j])
        heights.sort(reverse = True)
        # print(heights)
        total_steps = 0
        current_x, current_y = 0, 0
        while heights:
            target, next_x, next_y = heights.pop()
            current_steps = self.find_next(current_x, current_y, forest, target, m, n)
            if current_steps >= 0:
                # print(current_x, current_y, current_steps)
                total_steps += current_steps
                current_x, current_y = next_x, next_y
            else:
                return -1
        # print(forest)
        return total_steps
    
    
    def find_next(self, start_x, start_y, forest, target, m, n):
        steps = -1
        queue = collections.deque()
        queue.append([start_x, start_y])
        visited = set()
        visited.add((start_x, start_y))
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if forest[x][y] == target:
                    forest[x][y] = 1
                    return steps
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    adjx, adjy = x + dx, y + dy
                    if adjx < 0 or adjx >= m or adjy < 0 or adjy >= n:
                        continue
                    if forest[adjx][adjy] == 0 or (adjx, adjy) in visited:
                        continue
                    # if forest[adjx][adjy] > target:
                    #     continue
                    queue.append([adjx, adjy])
                    visited.add((adjx, adjy))
        return -1
                    
                    
                
        
        
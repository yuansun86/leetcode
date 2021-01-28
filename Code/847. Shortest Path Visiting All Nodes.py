class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = collections.deque()
        visited = set()
        N = len(graph)
        for i in range(N):
            queue.append((1 << i, i, 0))
            visited.add((1 << i, i))
        
        while queue:
            path, cur, dist = queue.popleft()
            if path == ((1 << N) - 1):
                return dist
            for neighbor in graph[cur]:
                newpath = path | 1 << neighbor
                if (newpath, neighbor) in visited:
                    continue
                queue.append((newpath, neighbor, dist + 1))
                visited.add((newpath, neighbor))
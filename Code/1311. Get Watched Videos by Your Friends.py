class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = collections.deque([id])
        visited = set([id])
        while queue:
            if level == 0:
                break
            for _ in range(len(queue)):
                current = queue.popleft()
                for neighbor in friends[current]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level -= 1
        freq = {}
        for node in queue:
            for movie in watchedVideos[node]:
                freq[movie] = freq.get(movie, 0) + 1
        temp = []
        for movie, count in freq.items():
            temp.append((count, movie))
        temp.sort()
        res = []
        for _, movie in temp:
            res.append(movie)
        return res
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                k = word[:i] + '*' + word[i + 1:]
                neighbors[k].append(word)
        
        print(neighbors)
        queue = collections.deque([beginWord])
        visited = set()
        visited.add(beginWord)
        distance = 1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                for i in range(len(current)):
                    k = current[:i] + '*' + current[i + 1:]
                    for neighbor in neighbors[k]:
                        if neighbor == endWord:
                            return distance
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
        return 0
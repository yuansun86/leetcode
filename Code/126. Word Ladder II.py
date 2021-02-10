class Solution:
    def generateDistance(self, endWord, wordList, graph):
        queue = collections.deque()
        queue.append(endWord)
        visited = set()
        visited.add(endWord)
        distancemap = {}
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                distancemap[current] = distance
                current_variation = self.generateVariation(current)
                for entry in current_variation:
                    for neighbor in graph[entry]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
        return distancemap
                
    def generateGraph(self, wordList):
        graph = collections.defaultdict(list)
        for word in wordList:
            word_variation = self.generateVariation(word)
            for entry in word_variation:
                graph[entry].append(word)
        return graph
    
    def generateVariation(self, word):
        results = []
        for i in range(len(word)):
            results.append(word[:i] + '*' + word[i + 1:])
        return results
    
    def generateNeighbors(self, word, graph):
        results = set()
        variations = self.generateVariation(word)
        for variation in variations:
            for neighbor in graph[variation]:
                if neighbor != word:
                    results.add(neighbor)
        return results
    
    def bfs(self, beginWord, endWord, wordList, graph, results):
        queue = collections.deque([[beginWord]])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_level = []
            for _ in range(len(queue)):
                previous_path = queue.popleft()
                current = previous_path[-1]
                neighbors = self.generateNeighbors(current, graph)
                for neighbor in neighbors:
                    if neighbor == endWord:
                        temp_result = previous_path + [neighbor]
                        results.append(temp_result)
                    if neighbor not in visited:
                        queue.append(previous_path + [neighbor])
                        current_level.append(neighbor)
            for item in current_level:
                visited.add(item)
            if results:
                break
                            
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = self.generateGraph(wordList)
        results = []
        self.bfs(beginWord, endWord, wordList, graph, results)
        return results
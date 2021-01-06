from collections import defaultdict, Counter, deque
class Solution:     
            
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = Counter({c : 0 for word in words for c in word})
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for c, d in zip(w1, w2):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(w2) < len(w1):
                    return ""
        
        results = []
        queue = deque([c for c in indegree if indegree[c] == 0])
        while queue:
            c = queue.popleft()
            results.append(c)
            for d in graph[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    queue.append(d)
        
        if len(results) != len(indegree):
            return ""
        return ''.join(results)
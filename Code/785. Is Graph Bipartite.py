class Solution:
    # BFS 诸层查找，分别查看是不是每一层都只在同一个set里面
    # 考虑到图的连通性，遍历每个节点，保存在visited里面
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def helper(graph, start, checked):
            setA = set()
            setB = set()
            checked.add(start)
            setA.add(start)
            queue = collections.deque()
            queue.append(start)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in setA:
                            return False
                        if neighbor in setB:
                            continue
                        else:
                            queue.append(neighbor)
                            setB.add(neighbor)
                            checked.add(neighbor)
                setA, setB = setB, setA
            return True
        
        n = len(graph)
        checked = set()
        for i in range(n):
            if i in checked:
                continue
            if not helper(graph, i, checked):
                return False
        return True
class Solution:
    def nextStrings(self, start):
        results = []
        for i in range(4):
            temp1 = start[:i] + str((int(start[i]) + 1) % 10) + start[i + 1:]
            temp2 = start[:i] + str((int(start[i]) - 1 + 10) % 10) + start[i + 1:]
            results.append(temp1)
            results.append(temp2)
        return results
        
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = collections.deque()
        visited = set()
        steps = -1
        queue.append("0000")
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return steps
                neighbors = self.nextStrings(current)
                for nei in neighbors:
                    if nei in dead or nei in visited:
                        continue
                    queue.append(nei)
                    visited.add(nei)
        return -1
        
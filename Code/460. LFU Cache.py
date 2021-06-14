class LFUCache:
    def __init__(self, capacity: int):
        self.keyToNode = {} # find Node via given key
        self.countToGroup = {} # find Counter Group via count number
        self.capacity = capacity
        self.size = 0
        self.headGroup = Group(-1)
        self.tailGroup = Group(1000)
        self.headGroup.next = self.tailGroup
        self.tailGroup.prev = self.headGroup
    
    def removeGroup(self, group):
        prev_group = group.prev
        next_group = group.next
        prev_group.next = next_group
        next_group.prev = prev_group
        del self.countToGroup[group.count]
    
    def addGroupAfter(self, old_group, new_group):
        next_group = old_group.next
        old_group.next = new_group
        new_group.prev = old_group
        new_group.next = next_group
        next_group.prev = new_group
        self.countToGroup[new_group.count] = new_group
    
    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        # print(node.key, node.count)
        old_group = self.countToGroup[node.count]
        old_group.removeNode(node)
        new_count = node.count + 1
        if new_count in self.countToGroup:
            new_group = self.countToGroup[new_count]
        else:
            new_group = Group(new_count)
            self.addGroupAfter(old_group, new_group)
            self.countToGroup[new_count] = new_group
        new_group.addNode(node)
        if old_group.size == 0:
            self.removeGroup(old_group)
        # print(key, self.countToGroup)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            old_group = self.countToGroup[node.count]
            old_group.removeNode(node)
            new_count = node.count + 1
            if new_count in self.countToGroup:
                new_group = self.countToGroup[new_count]
            else:
                new_group = Group(new_count)
                self.addGroupAfter(old_group, new_group)
                self.countToGroup[new_count] = new_group
            new_group.addNode(node)
            if old_group.size == 0:
                self.removeGroup(old_group)
        else:
            if self.size == self.capacity:  
                to_remove_group = self.headGroup.next
                to_remove_node = to_remove_group.popLRU()
                del self.keyToNode[to_remove_node.key]
                if to_remove_group.size == 0:
                    self.removeGroup(to_remove_group)
                self.size -= 1
            node = Node(key, value)
            self.keyToNode[key] = node
            if 1 not in self.countToGroup:
                new_group = Group(1)
                self.addGroupAfter(self.headGroup, new_group)
                self.countToGroup[1] = new_group
            else:
                new_group = self.countToGroup[1]
            new_group.addNode(node) 
            self.size += 1
            
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.count = 1

        
class Group:
    def __init__(self, count):
        self.count = count
        self.prev = None
        self.next = None
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
    
    
    def addNode(self, node):
        prev_front = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = prev_front
        prev_front.prev = node
        node.count = self.count
        self.size += 1
    
    def popLRU(self):
        to_remove = self.tail.prev
        prev_to_remove = to_remove.prev
        prev_to_remove.next = self.tail
        self.tail.prev = prev_to_remove
        self.size -= 1
        return to_remove

        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
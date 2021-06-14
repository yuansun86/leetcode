class FileSystem:

    def __init__(self):
        self.root = Item('root', isFile = False)

    def ls(self, path: str) -> List[str]:
        nodePath = path.split('/')
        cur_node = self.root
        for node_name in nodePath:
            if not node_name:
                continue
            cur_node = cur_node.dir[node_name]
        if cur_node.isFile == True:
            return [cur_node.name]
        else:
            res = []
            for node_name in cur_node.dir:
                res.append(node_name)
            res.sort()
            return res

    def mkdir(self, path: str) -> None:
        pathNodes = path.split('/')
        cur_node = self.root
        for node_name in pathNodes:
            if not node_name:
                continue
            if node_name in cur_node.dir:
                cur_node = cur_node.dir.get(node_name)
            else:
                node = Item(node_name, isFile = False)
                cur_node.dir[node_name] = node
                cur_node = cur_node.dir.get(node_name)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        pathNodes = filePath.split('/')
        cur_node = self.root
        for i, node_name in enumerate(pathNodes):
            if not node_name:
                continue
            if node_name in cur_node.dir:
                if i == len(pathNodes) - 1:
                    # last level, file, write content
                    node = cur_node.dir[node_name]
                    node.content += content
                    return
                else:
                    # not last level, dir
                    cur_node = cur_node.dir[node_name]
            else:
                if i == len(pathNodes) - 1:
                    # last level, create file, put it in parent dir
                    node = Item(node_name, isFile = True)
                    node.content = content
                    cur_node.dir[node_name] = node
                    return
                else:
                    # not last level, create dir, put it in parent dir
                    node = Item(node_name, isFile = False)
                    node.parent = cur_node
                    cur_node.dir[node_name] = node
                    cur_node = node

    def readContentFromFile(self, filePath: str) -> str:
        nodePath = filePath.split('/')
        cur_node = self.root
        for node_name in nodePath:
            if not node_name:
                continue
            cur_node = cur_node.dir[node_name]
        return cur_node.content

class Item:
    
    def __init__(self, name, isFile):
        self.name = name
        self.content = None
        self.isFile = isFile
        self.dir = {} # key = name, val = node
        self.parent = None
    
    
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.previous = self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.previous = self.left
        
    def insert(self,node):
        prev = self.right.previous
        self.right.previous = node
        prev.next = node
        node.next = self.right
        node.previous = prev
        
    def remove(self,node):
        prev = node.previous
        nxt = node.next
        prev.next = nxt
        nxt.previous = prev
    
    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            
        node = Node(key,value)
        self.hashMap[key] = node
        self.insert(self.hashMap[key])
        
        if len(self.hashMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashMap[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
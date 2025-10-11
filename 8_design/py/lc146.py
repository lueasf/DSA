# LRU Cache implementationb (Least Recently Used)

"""
The basic idea is : we have a table and we can delete the least recently used item from it if needed.

get(int key) Return the value of the key if the key exists, otherwise return -1.
put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity 
from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Issue : 
- a simple hashmap won't work because we need to keep track of the order of usage.
- a list won't work because we need O(1) access time. (O(n) for list search).

Solution : combine a hashmap and a doubly linked list.

Head : most recently used (MRU)
Tail : least recently used (LRU)

Schema : 
Hashmap : {key : pointer to node in DLL}
DLL : [MRU] <-> [node1] <-> ... <-> [nodeN] <-> [LRU]

for example, the cache can be : 
self.cache = {
    1: [Node(key=1, value=10)],
    2: [Node(key=2, value=20)]
}

By doing a schema, it's really easy.

Application : 
- Caching
- Web browsers
- File systems
- Database management systems
"""

class Node:
    __slots__ = ('key', 'value', 'prev', 'next') # only values
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Hash Map : key -> node 

        self.left = Node() # pointer to MRU/head
        self.right = Node() # pointer to LRU/tail

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def insert(self, node: Node) -> None:
        # between self.left and its next : MRU
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
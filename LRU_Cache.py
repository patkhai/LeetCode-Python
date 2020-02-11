'''

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''
'''
Approach : Fast lookup = Hashtable 
           Fast removal = Double LinkedList 
Doubly Linked List: This will hold the items that our cache has. We will have n items in the cache.

This structure satisfies the constraint for fast addition since any doubly linked list item can be 
added or removed in O(1) time with proper references.

Hashtable: The hashtable will give us fast access to any item in the doubly linked list items to avoid O(n) search for items 
and the LRU entry (which will always be at the tail of the doubly linked list).

This is a very common pattern, we use a structure to satisfy special insertion or remove properties (use a BST, linked list, etc.) 
and back it up with with a hashtable so we do not re-traverse the structures every time to find elements.

 
'''
class Node: 
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.prev = None 
        self.next = None 
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {} 
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail #head points to tail
        self.tail.prev = self.head  #tail points to head 
    
    def get(self, key):
        'if key in dic, node = the key '
        if key in self.dic: 
            node = self.dic[key]
            'remove the node'
            self.remove(node)
            'add the node into most recent position'
            self.addNode(node)
            return node.value
        return -1     

    def put(self, key, value):
        'if key in dic, remove the key meaing old value'
        if key in self.dic: 
            self.remove(self.dic[key])
        'create new node'
        node = Node(key, value)
        self.addNode(node)
        self.dic[key] = node 
        
        'if lenght of dic is greater than capacity'
        if len(self.dic) > self.capacity: 
            node = self.head.next 
            'remove the oldest node'
            self.remove(node)
            del self.dic[node.key]
           
    def remove(self,node):
        'remove the node' 
        prev = node.prev 
        next = node.next
        prev.next = next 
        next.prev = prev 
    
    def addNode(self, node): 
        'insert new node into last position'
        prev = self.tail.prev 
        prev.next = node 
        self.tail.prev = node 
        node.prev = prev 
        node.next = self.tail
        

s = LRUCache(2)

print(s.put(1,1))
print(s.put(2,2))
print(s.get(1))
print(s.put(3,3))
print(s.get(2))
print(s.put(4,4))
print(s.get(1))
print(s.get(3))
print(s.get(4))

#[null,null,null,1,null,-1,null,-1,3,4]
class Node:
    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = {}
        self.leftLeast = Node(0,0)
        self.rightMost = Node(0, 0)

        self.leftLeast.next = self.rightMost
        self.rightMost.prev = self.leftLeast
        
    #Node is middle Node
    def remove(self, node):
       prev = node.prev
       nxt = node.next

       prev.next = nxt
       nxt.prev = prev


    #Node is the middle Node
    def insert(self, node):
        prev = self.rightMost.prev

        prev.next = node
        node.prev = prev
        node.next = self.rightMost
        self.rightMost.prev = node

    
    def get(self, key: int) -> int:
        if key in self.count:
            self.remove(self.count[key])
            self.insert(self.count[key])
            return self.count[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.count:
            self.remove(self.count[key])
        
        self.count[key] = Node(key, value)
        self.insert(self.count[key])

        if len(self.count) > self.capacity:
            leastRecent = self.leftLeast.next
            self.remove(leastRecent)
            del self.count[leastRecent.key]

        
         

        
        

        


            


        

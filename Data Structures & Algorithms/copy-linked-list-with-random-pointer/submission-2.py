"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if (head == None):
            return None
        #Create hashmap variables
        randList = {}
        curr = head

        while (curr):
            randList[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while (curr):
            randList[curr].next = randList.get(curr.next)
            randList[curr].random = randList.get(curr.random)
            curr = curr.next

        
        return randList[head]
        
        
        

        
        


        
       



            


        
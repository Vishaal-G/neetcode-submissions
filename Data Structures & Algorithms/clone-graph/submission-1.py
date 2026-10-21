"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        newOld = {}
        def cloneGraphHelper(node):
            if node in newOld:
                return
            
            newOld[node] = Node(node.val)
            for nei in node.neighbors:
                cloneGraphHelper(nei)
        
        cloneGraphHelper(node)

        for oldNode, newNode in newOld.items():
            for neighbor in oldNode.neighbors:
                newNode.neighbors.append(newOld[neighbor])
        
        return newOld[node]
        

            
            

        
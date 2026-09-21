# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        Q = []
        P = []

        Q.append(q)
        P.append(p)

        while Q and P:
            valQ = Q.pop(0)
            valP = P.pop(0)

            if valQ == None and valP == None:
                continue

            if valQ is None or valP is None:
                return False
            
            if valQ.val != valP.val:
                return False
            
            Q.append(valQ.left)
            Q.append(valQ.right)
            P.append(valP.left)
            P.append(valP.right)
            
        return True

        

        
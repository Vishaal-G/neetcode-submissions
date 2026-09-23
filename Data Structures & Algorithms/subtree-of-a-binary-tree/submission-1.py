# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtreeHelper(self, root, subRoot):
        QRoot = deque([root])
        QSubRoot = deque([subRoot])

        while QRoot and QSubRoot:
            valRoot = QRoot.popleft()
            valSubRoot = QSubRoot.popleft()

            if valRoot == None and valSubRoot == None:
                continue
            if valRoot == None or valSubRoot == None:
                return False
            if valRoot.val != valSubRoot.val:
                return False
            
            else:
                QRoot.append(valRoot.left)
                QRoot.append(valRoot.right)
                QSubRoot.append(valSubRoot.left)
                QSubRoot.append(valSubRoot.right)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None):
            return False
        
        return self.isSubtreeHelper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    






        
    
        
                        
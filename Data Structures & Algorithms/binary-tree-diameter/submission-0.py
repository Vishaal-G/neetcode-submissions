# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTreeHelper(self, root):
        if root == None:
            return -1
        
        v1 = self.diameterOfBinaryTreeHelper(root.left)
        v2 = self.diameterOfBinaryTreeHelper(root.right)

        self.longPath = max(self.longPath, (v1+1) + (v2+1))

        return max(v1,v2) + 1

    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longPath = 0
        self.diameterOfBinaryTreeHelper(root)

        return self.longPath

        
        
        

        
        
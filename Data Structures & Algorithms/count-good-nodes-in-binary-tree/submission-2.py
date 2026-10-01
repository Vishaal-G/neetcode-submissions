# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesHelper(self, root, big):
        if root == None:
            return 
        
        if (root.val >= big):
            self.goodCount += 1
        
        big = max(big, root.val)
        
        self.goodNodesHelper(root.left, big)
        self.goodNodesHelper(root.right, big)

        return self.goodCount

    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0
        big = -101
        self.goodNodesHelper(root, big)
        return self.goodCount
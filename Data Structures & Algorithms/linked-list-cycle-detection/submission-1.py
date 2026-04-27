# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return False 
        
        currentOnePass = head
        currentTwoPass = head
        while (currentTwoPass != None and currentTwoPass.next != None):
            currentOnePass = currentOnePass.next
            currentTwoPass = currentTwoPass.next.next
            if (currentOnePass == currentTwoPass):
                return True  
        return False
        
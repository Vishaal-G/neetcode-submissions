# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (head == None or head.next == None or head.next.next == None):
            return
        
        fast = head
        prevFast = head
        slow = head

        while(fast != None):
            if (fast.next == None):
                temp = slow.next
                slow.next = fast
                if (fast == temp):
                    break
                fast.next = temp
                slow = temp
                fast = temp
                prevFast.next = None
                prevFast = temp
            else:
                prevFast = fast
                fast = fast.next

        
        
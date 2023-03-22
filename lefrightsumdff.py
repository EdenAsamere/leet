# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # initialize prev as None since first node will become last node after reversal
        prev = None 
        
        # loop until we reach the end of the linked list
        while head:
            # store current node in cur
            cur = head
            
            # update head to next node
            head = head.next
            
            # change direction of link for current node
            cur.next = prev
            
            # update prev to current node for next iteration
            prev = cur
        
        # prev will be the new head of the reversed list
        print(prev)

head=[1,2,3,4,5]
print(reverseList(head))

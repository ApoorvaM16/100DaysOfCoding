# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, count  = head, 0
        while current:
            count +=1
            current = current.next
        mid = (count // 2)

        current, counter = head, 0
        while current.next:
            if counter == mid -1:
                
                current.next = current.next.next
                return head
            counter +=1
            current = current.next
            


        
        
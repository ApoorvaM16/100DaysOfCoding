# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        count, current = 0, head
        
        while current:
            current = current.next
            count +=1
        mid = (count // 2)
        
        counter, current = 0, head
        while current:
            if counter == mid:
                return current
            current = current.next
            counter +=1

        
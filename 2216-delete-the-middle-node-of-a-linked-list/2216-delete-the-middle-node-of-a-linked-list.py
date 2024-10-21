# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # optimal solution

        if not head or not head.next:
            return None
        slow = fast = head
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
        
        slow.next = slow.next.next
        return head



        # current, count  = head, 0
        # while current:
        #     count +=1
        #     current = current.next
        # mid = (count // 2)

        # current, counter = head, 0
        # while current.next:
        #     if counter == mid -1:
                
        #         current.next = current.next.next
        #         return head
        #     counter +=1
        #     current = current.next
            


        
        
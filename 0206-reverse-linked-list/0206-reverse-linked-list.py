# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using recursion

        if head is None or head.next is None:
            return head
        
        current = head
        newHead = self.reverseList(current.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead












        # if head is None or head.next is None:
        #     return head
        # newHead = self.reverseList(head.next)
        # front = head.next
        # front.next = head
        # head.next = None
        # return newHead


        # if head == None or head.next == None:
        #     return head
        # current, prev = head, None
        # while current:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        # return prev
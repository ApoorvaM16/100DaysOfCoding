# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next is None:
            return None
        if n == 1 and head.next.next is None:
            head.next = None
            return head
        def lengthLL(head):
            current, count = head, 0
            while current:
                current = current.next
                count +=1

            return count

        length = lengthLL(head)
        counter, count = length - n, 0
        if counter == 0:
            return head.next
        current = head
        while current:
            count +=1
            if counter == count:
                current.next = current.next.next
                return head
            current = current.next
        
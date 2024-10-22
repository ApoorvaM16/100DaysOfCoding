# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return [0]
        carry,ll1,ll2 = 0,l1,l2
        dummyNode = ListNode(-1)
        current = dummyNode
        while ll1 or ll2 or carry:
            sum = carry
            if ll1: sum += ll1.val
            if ll2: sum += ll2.val

            
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            
            if ll1: ll1 = ll1.next
            if ll2: ll2 = ll2.next
        
        
        return dummyNode.next

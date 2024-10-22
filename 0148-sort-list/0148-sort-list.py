# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left,right):
        leftCur = left
        rightCur = right
        dummyNode = ListNode(-1)
        temp = dummyNode
        while leftCur and rightCur:
            if leftCur.val <= rightCur.val:
                temp.next = leftCur
                temp = leftCur
                leftCur = leftCur.next
            else:
                temp.next = rightCur
                temp = rightCur
                rightCur = rightCur.next

            if(leftCur): temp.next = leftCur
            else: temp.next = rightCur
        return dummyNode.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        def findMiddle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
           

        
        middle = findMiddle(head)
        right = middle.next
        middle.next = None
        left = head

        leftHead = self.sortList(left)
        rightHead = self.sortList(right)
        return self.merge(leftHead,rightHead)

        # current, arr = head, []
        # while current:
        #     arr.append(current.val)
        #     current = current.next
        # arr.sort()
        # current = head
        # for i in arr:
        #     current.val = i
        #     current = current.next
        # return head
        
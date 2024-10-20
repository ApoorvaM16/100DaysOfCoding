# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     # 2. reverse sencond part
    


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # optimal O(1), O(n)
        # 1. Find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        def reverseLL(temp):
            if temp is None or temp.next is None:
                return temp
            newHead = reverseLL(temp.next)
            front = temp.next
            front.next = temp
            temp.next = None
            return newHead

        newHead = reverseLL(slow.next)  

        # 3. compare
        first = head
        second = newHead
        while second:
            if first.val != second.val:
                reverseLL(newHead)
                return False
            first = first.next
            second = second.next
        reverseLL(newHead)
        return True



        # current, arr = head, []
        # while current:
        #     arr.append(current.val)
        #     current = current.next
        # return arr == arr[::-1]
        
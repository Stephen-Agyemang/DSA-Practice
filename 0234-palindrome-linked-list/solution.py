# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        if not head or not head.next:
            return True 

        fast = head
        slow = head

        while fast.next and fast.next.next:

            fast = fast.next.next
            slow = slow.next
        
        prev_slow = None
        curr_slow = slow.next  

        while curr_slow:
            curr_next = curr_slow.next
            curr_slow.next = prev_slow

            prev_slow = curr_slow
            curr_slow = curr_next

        right = prev_slow
        left = head

        while right:

            if right.val != left.val:
                return False
            right = right.next
            left = left.next

        return True 


        

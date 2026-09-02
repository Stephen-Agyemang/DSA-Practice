# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        fast = head 
        slow = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow 
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
             
            prev = curr    
            curr = next_node

        curr_right = prev
        curr_left = head

        while curr_right:
            if curr_right.val != curr_left.val:
                return False 

            curr_right = curr_right.next
            curr_left = curr_left.next


        return True

            

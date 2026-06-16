# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        if not head:
            return None

        stack = []
        current_node = head

        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next

        right = len(stack) - 1
        left = 0
        while left < right:

            if stack[left] != stack[right]:
                return False
            right -= 1
            left += 1

        return True 


        

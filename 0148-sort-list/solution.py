# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None 

        curr = head
        lst = []

        while curr:
            lst.append(curr.val)
            curr = curr.next

        lst.sort()
        newHead = ListNode(lst[0])
        curr_node = newHead

        for num in lst[1:]:
            curr_node.next = ListNode(num)
            curr_node = curr_node.next

        return newHead








        

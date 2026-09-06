# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 

        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head


        # dummy = ListNode(float('inf'))
        # curr_dummy = dummy

        # while head:
        #     if head.val != curr_dummy.val:
        #         curr_dummy.next = ListNode(head.val)
        #         curr_dummy = curr_dummy.next

        #     head = head.next

        # return dummy.next

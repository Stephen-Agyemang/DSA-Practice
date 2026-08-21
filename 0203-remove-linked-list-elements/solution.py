# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        # dummy = ListNode(-1, None)
        # curr_dummy = dummy
        # curr_ll = head

        # while curr_ll:

        #     temp = curr_ll.next

        #     if curr_ll.val != val:
        #         curr_ll.next = None
        #         curr_dummy.next = curr_ll
        #         curr_dummy = curr_dummy.next

        #     curr_ll = temp

        # return dummy.next


        dummy = ListNode(-1)
        dummy.next = head 

        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next 

        return dummy.next

                

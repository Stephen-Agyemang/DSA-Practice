# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        fast = head 
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(slow)

        return self.merger(list1, list2)


    def merger(self, list1: Optioinal[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy 

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1

        else:
            curr.next = list2

        return dummy.next

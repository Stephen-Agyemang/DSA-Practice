# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_ll(head):

        if not head:
            return None

        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        return prev 

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr_1 = reverse_ll(l1)
        curr_2 = reverse_ll(l2)
        str_1 = ""
        str_2 = ""

        while curr_1:
            str_1 += str(curr_1.val)
            curr_1 = curr_1.next

        while curr_2:
            str_2 += str(curr_2.val)
            curr_2 = curr_2.next

        print(str_1)
        print(str_2)

        answer = int(str_1) + int(str_2)
        print(answer)

        answer_list = list(str(answer))
        print(answer)

        newHead = ListNode(int(answer_list.pop()))
        curr = newHead

        while answer_list:
            digit = int(answer_list.pop())
            curr.next = ListNode(digit)
            curr = curr.next

        return newHead
            





        

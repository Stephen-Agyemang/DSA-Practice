# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse_ll(head):

#         if not head:
#             return None

#         curr = head
#         prev = None

#         while curr:
#             next_node = curr.next
#             curr.next = prev

#             prev = curr
#             curr = next_node
#         return prev 

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # curr_1 = reverse_ll(l1)
        # curr_2 = reverse_ll(l2)
        # str_1 = ""
        # str_2 = ""

        # while curr_1:
        #     str_1 += str(curr_1.val)
        #     curr_1 = curr_1.next

        # while curr_2:
        #     str_2 += str(curr_2.val)
        #     curr_2 = curr_2.next

        # answer = int(str_1) + int(str_2)

        # answer_list = list(str(answer))

        # newHead = ListNode(int(answer_list.pop()))
        # curr = newHead

        # while answer_list:
        #     digit = int(answer_list.pop())
        #     curr.next = ListNode(digit)
        #     curr = curr.next

        # return newHead

        dummy = ListNode(-1)
        current = dummy

        carry = 0 

        while l1 or l2 or carry:

            if l1:
                val1 = l1.val 
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0 

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit) 
            current = current.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next 

        return dummy.next






        

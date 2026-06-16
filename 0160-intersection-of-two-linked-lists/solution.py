# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ## We want to get to the node where the point in the two linkedlist where the nodes point to the same in memory.
        ## We might want to go through both separately or in a specific sequence so that we can get to that point in all the lists

        if not headA and headB:
            return None

        curr_a = headA
        curr_b = headB

        dct = {}

        while curr_a:
            if curr_a not in dct:
                dct[curr_a] = 1

            else:
                dct[curr_a] += 1

            curr_a = curr_a.next

        while curr_b:
            if curr_b not in dct:
                dct[curr_b] = 1

            else:
                return curr_b
                
            curr_b = curr_b.next

        return None


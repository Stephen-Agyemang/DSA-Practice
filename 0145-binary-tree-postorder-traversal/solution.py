# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        lst = []

        if not root:
            return lst

        if root:
            lst.extend(self.postorderTraversal(root.left))
            lst.extend(self.postorderTraversal(root.right))
            lst.append(root.val)

        return lst

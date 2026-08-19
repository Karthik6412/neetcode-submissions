# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high): # low and high are boundaries here
            if node is None:
                return True
            if not node.val > low or not node.val < high:
                return False
            
            lcheck = valid(node.left, low, node.val) 
            rcheck = valid(node.right, node.val, high)

            return lcheck and rcheck
    
        return valid(root, float("-inf"), float("+inf"))

            

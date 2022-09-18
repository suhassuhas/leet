# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def revOddLevel(root1,root2,level):
            if root1 == None or root2 == None:
                return
            if root1.left == None and root1.right == None:
                return 
            if root2.left == None and root2.right == None:
                return  
            if level % 2 == 0:
                root1.left.val ,root2.right.val = root2.right.val , root1.left.val
            revOddLevel(root1.left,root2.right,level+1)
            revOddLevel(root1.right,root2.left,level+1)
            
        revOddLevel(root,root,0)
        return root
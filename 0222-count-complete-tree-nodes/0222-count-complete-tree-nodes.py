# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = []
        q.append(root)
        level = 0
        while len(q) != 0:
            size = len(q)
            if size != (2**level):
                count+=size
                break
            while size>0:
                curr = q.pop(0)
                if curr == None:
                    break
                count+=1
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
                size-=1
            level+=1
        return count
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lsum=0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.lsum
        else:
            if root.left:
                if not root.left.left and not root.left.right:
                    self.lsum+=root.left.val
                self.lsum=self.sumOfLeftLeaves(root.left)
            if root.right:
                self.lsum=self.sumOfLeftLeaves(root.right)
            return self.lsum

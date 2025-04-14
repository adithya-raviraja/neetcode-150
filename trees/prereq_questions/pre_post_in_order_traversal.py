# Question Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.inorder_list = list()
        self.preorder_list = list()
        self.postorder_list = list()

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.inorderTraversal(root.left)
        self.inorder_list.append(root.val)
        self.inorderTraversal(root.right)

        return self.inorder_list
    
    def preorderTraversal(self, root):
        if not root:
            return []
        
        self.preorder_list.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.preorder_list
    
    def postorderTraversal(self, root):
        if not root:
            return []
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.postorder_list(root.val)

        return self.postorder_list

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
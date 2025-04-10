# Question Link: https://leetcode.com/problems/delete-node-in-a-bst/
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findMinNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr
    
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.findMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root



if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
# Question Link: https://neetcode.io/problems/kth-smallest-integer-in-bst
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.inorder_arr = list()

    def inorder(self, root):
        if not root:
            return []
        
        self.inorder(root.left)
        self.inorder_arr.append(root.val)
        self.inorder(root.right)
        return
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.inorder_arr[k - 1]
    

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
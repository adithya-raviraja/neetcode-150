# Question Link: https://neetcode.io/problems/invert-a-binary-tree
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        temp = None
        if not curr:
            return None
        
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
    
        self.invertTree(curr.left)
        self.invertTree(curr.right)
        
        return root
        



if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
# Question Link: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre_idx = 0
        self.preorder = list()
        self.inorder = list()
        self.idx_hash_map = dict()
        return
    
    def dfs(self, l, r):
        if l > r:
            return None
        
        root_val = self.preorder[self.pre_idx]
        self.pre_idx += 1

        root = TreeNode(root_val)
        mid = self.idx_hash_map[root_val]
        
        root.left = self.dfs(l, mid - 1)
        root.right = self.dfs(mid + 1, r)

        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.preorder = preorder
        self.idx_hash_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        return self.dfs(0, len(preorder) - 1)

            

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
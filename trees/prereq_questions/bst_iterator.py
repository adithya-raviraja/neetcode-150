# Question Link: https://leetcode.com/problems/binary-search-tree-iterator/description/
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = list()
        self.inorder = list()
        self.curr = root
        self.counter = 0

        while self.curr or self.stack:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                self.curr = self.stack.pop()
                self.inorder.append(self.curr.val)
                self.curr = self.curr.right
        
        return


    def next(self):
        """
        :rtype: int
        """
        val = self.inorder[self.counter]
        self.counter += 1
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.counter == len(self.inorder):
            return False
        else:
            return True
        
if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
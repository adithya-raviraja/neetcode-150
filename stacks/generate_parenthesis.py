# Question Link: https://leetcode.com/problems/generate-parentheses/
from typing import *

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = list()
        res = list()

        def traverse_array(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return
            
            if open_count < n:
                stack.append('(')
                traverse_array(open_count+1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(')')
                traverse_array(open_count, close_count+1)
                stack.pop()

        
        traverse_array(0, 0)
        return res

if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
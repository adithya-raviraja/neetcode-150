# Question Link: https://leetcode.com/problems/implement-queue-using-stacks/description/
from typing import *

class MyQueue(object):

    def __init__(self):
        self.main_stack = list()
        self.stack_2 = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.main_stack) == 0:
            self.main_stack.append(x)
            return
        
        while len(self.main_stack) > 0:
            self.stack_2.append(self.main_stack.pop())

        self.main_stack.append(x)

        while len(self.stack_2) > 0:
            self.main_stack.append(self.stack_2.pop())

        self.stack_2 = list()
        return

    def pop(self):
        """
        :rtype: int
        """
        val = self.main_stack.pop()
        return val

    def peek(self):
        """
        :rtype: int
        """
        return self.main_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.main_stack) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(10)
    obj.push(20)
    obj.push(30)
    print(obj.peek())
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
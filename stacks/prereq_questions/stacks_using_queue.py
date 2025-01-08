# Question Link: https://leetcode.com/problems/implement-stack-using-queues/
from typing import *
import copy

class MyStack(object):

    def __init__(self):
        self.queue_main = list()
        self.queue_2 = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_main.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue_main) != 1:
            self.queue_2.append(self.queue_main.pop(0))

        last = self.queue_main.pop(0)
        self.queue_main = copy.deepcopy(self.queue_2)
        self.queue_2 = list()
        return last
        
        

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue_main) != 1:
            self.queue_2.append(self.queue_main.pop(0))

        last = self.queue_main[-1]
        self.queue_2.append(self.queue_main.pop(0))
        self.queue_main = copy.deepcopy(self.queue_2)
        self.queue_2 = list()
        return last

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue_main) != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    stack = MyStack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.top())
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
    print(stack.pop())
    print(stack.empty())

    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
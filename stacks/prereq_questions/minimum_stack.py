# Question Link:
import sys
from typing import *

class MinStack(object):

    def __init__(self):
        self.stack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn = min(self.stack[-1][1], val)
            self.stack.append((val, mn))
        return


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        return
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        

if __name__ == "__main__":
    minstack = MinStack()
    res = list()
    res.append(minstack.push(1))
    res.append(minstack.push(0))
    res.append(minstack.push(2))
    res.append(minstack.getMin())
    res.append(minstack.pop())
    res.append(minstack.pop())
    res.append(minstack.top())
    res.append(minstack.getMin())

    print(res)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
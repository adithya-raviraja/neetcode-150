# Question Link: https://leetcode.com/problems/baseball-game/
from typing import *

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = list()
        integer = False
        for op in operations:
            try:
                op = int(op)
                integer = True
            except ValueError as e:
                pass

            if integer:
                stack.append(op)
            else:
                if op == '+':
                    val1 = stack[-1]
                    val2 = stack[-2]
                    stack.append(val1+val2)
                elif op == 'D':
                    prev_val = stack[-1]
                    stack.append(prev_val * 2)
                elif op == 'C':
                    stack.pop()
                else:
                    pass

            integer = False
        
        sum = 0
        while len(stack) > 0:
            sum += stack.pop()

        return sum

if __name__ == "__main__":
    ops = ["1","C"]
    output = Solution().calPoints(ops)
    print('OUTPUT: ', output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
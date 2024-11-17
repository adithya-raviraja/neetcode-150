# Question Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import *

VALID_OPERATORS = ['+', '-', '/', '*']
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for token in tokens:
            if token not in VALID_OPERATORS:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    res = num2 + num1
                elif token == '-':
                    res = num2 - num1
                elif token == '/':
                    res = int(num2 / num1)
                else:
                    res = num2 * num1
                
                stack.append(res)
        
        return stack.pop()

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    output = Solution().evalRPN(tokens)
    print('Output: ', output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
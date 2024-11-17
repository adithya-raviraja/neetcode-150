# Question Link: https://leetcode.com/problems/valid-parentheses/
from typing import *

OPEN_BRACKETS = ['(', '{', '[']
CLOSE_BRACKETS = [')', '}', ']']
MATCHING_CLOSE_BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

class Solution(object):
    def isValid(self, s):
        stack = list()
        input_list = list(s)

        if len(input_list) == 1:
            return False

        for entry in input_list:
            if entry in OPEN_BRACKETS:
                stack.append(entry)
            elif entry in CLOSE_BRACKETS:
                if len(stack) == 0:
                    return False
                if MATCHING_CLOSE_BRACKETS[stack[-1]] == entry:
                    stack.pop()
                else:
                    return False
            else:
                continue

        if len(stack) > 0:
            return False
        else:
            return True



if __name__ == "__main__":
    input = "(("
    output = Solution().isValid(input)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
# Question Link: https://leetcode.com/problems/decode-string/description/
from typing import *

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        decode_stack = list()
        cur_string = ''
        cur_num = 0

        for entry in s:
            if entry == '[':
                decode_stack.append(cur_string)
                decode_stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif entry == ']':
                prev_num = decode_stack.pop()
                prev_string = decode_stack.pop()
                cur_string = prev_string + cur_string * prev_num
            elif entry.isdigit():
                cur_num = cur_num * 10 + int(entry)
            else:
                cur_string += entry
        
        return cur_string

if __name__ == "__main__":
    s = "3[a2[c]]"
    output = Solution().decodeString(s)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
# Question Link: https://neetcode.io/problems/longest-substring-without-duplicates
from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = float('-inf')
        L = 0

        for R in range(len(s)):
            while s[R] in substring:
                substring.remove(s[L])
                L += 1

            substring.add(s[R])
            length = max(length, R - L + 1)
            
        return 0 if length == float('-inf') else length


if __name__ == "__main__":
    s = "xxxx"
    output = Solution().lengthOfLongestSubstring(s)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
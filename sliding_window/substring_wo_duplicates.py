# Question Link: https://neetcode.io/problems/longest-substring-without-duplicates
from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = dict()
        r = 0
        l = 0
        res = 0
        
        
        for r in range(len(s)):
            if s[r] not in unique_chars:
                unique_chars[s[r]] = 1
            else:
                while s[l] in unique_chars:
                    unique_chars.pop(s[l], None)
                    l += 1

            res = max(res, len(unique_chars.keys()))            
        return res
        
        

if __name__ == "__main__":
    s = 'zxyzxyz'
    output = Solution().lengthOfLongestSubstring(s)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(m)')
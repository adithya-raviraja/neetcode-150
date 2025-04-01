# Question Link: https://neetcode.io/problems/longest-repeating-substring-with-replacement
from typing import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        r = 0
        l = 0
        maxf = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        
        return res

if __name__ == "__main__":
    s = "AAABABB"
    k = 1
    
    output = Solution().characterReplacement(s, k)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(m)')
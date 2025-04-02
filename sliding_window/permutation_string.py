# Question Link: https://neetcode.io/problems/permutation-string
from typing import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        matches = 0
        
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
                
            
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
                
            l += 1
            
        return matches == 26
            


if __name__ == "__main__":
    s1 = 'abc'
    s2 = 'lecabee'
    
    output = Solution().checkInclusion(s1, s2)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1*26)')
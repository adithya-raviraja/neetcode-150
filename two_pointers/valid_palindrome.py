# Question Link: https://neetcode.io/problems/is-palindrome
from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left = left + 1
                continue
            elif not s[right].isalnum():
                right = right - 1
                continue
            else:
                pass
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1

        return True

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    output = Solution().isPalindrome(s)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')
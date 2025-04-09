# Question Link: https://neetcode.io/problems/minimum-window-with-characters
from typing import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        res = [-1, -1]
        res_len = float('infinity')
        window = {}
        freq_t = {}

        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)

        have = 0
        need = len(freq_t)
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in freq_t and window[char] == freq_t[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float('infinity') else ""



if __name__ == "__main__":
    s="ADOBECODEBANC"
    t="ABC"

    output = Solution().minWindow(s, t)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(t)')
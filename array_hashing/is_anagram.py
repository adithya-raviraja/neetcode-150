from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        s_dict = dict()
        t_dict = dict()

        if len(s) != len(t):
            return False
        
        index = 0
        while index < len(s):
            s_dict[s[index]] = 1 + s_dict.get(s[index], 0)
            t_dict[t[index]] = 1 + t_dict.get(t[index], 0)
            index += 1

        return s_dict == t_dict

if __name__ == "__main__":
    s = "bbcc"
    t = "ccbc"

    output = Solution().isAnagram(s,t)
    print(output)

    s = "jar"
    t = "jam"
    output = Solution().isAnagram(s,t)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
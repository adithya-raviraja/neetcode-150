# Question Link: https://neetcode.io/problems/longest-consecutive-sequence
from typing import *
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        chain = 0

        for num in hash_set:
            if (num - 1) not in hash_set:
                length = 1
                while (num + length) in hash_set:
                    length += 1
                chain = max(length, chain)

        return chain

if __name__ == "__main__":
    nums = [0,3,2,5,4,6,1,1]
    output = Solution().longestConsecutive(nums)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
# Question Link: https://neetcode.io/problems/find-duplicate-integer
from typing import *
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')
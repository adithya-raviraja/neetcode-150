# Question Link: https://neetcode.io/problems/car-fleet
from typing import *

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merge_arr = [(p, s) for p, s in zip(position, speed)]
        merge_arr.sort(reverse=True)
        stack = []

        for position, speed in merge_arr:
            stack.append((target-position)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

if __name__ == "__main__":
    target = 10
    position = [1,4]
    speed = [3,2]
    output = Solution().carFleet(target, position, speed)
    print(output)
    print('TIME COMPLEXITY: O(nlogn)')
    print('SPACE COMPLEXITY: O(n)')
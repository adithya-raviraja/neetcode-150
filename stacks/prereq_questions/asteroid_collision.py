# Question Link: https://leetcode.com/problems/asteroid-collision/
from typing import *

class Solution(object):
    def getDirection(self, asteroid):
        if asteroid > 0:
            return 'right'
        else:
            return 'left'

    def OpDirection(self, direction):
        if direction == 'left':
            return 'right'
        else:
            return 'left'

    def absValue(self, asteroid):
        return abs(asteroid)

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        collision_stack = list()
        for asteroid in asteroids:
            if len(collision_stack) == 0:
                collision_stack.append(asteroid)
                continue

            while (collision_stack) and (asteroid < 0 < collision_stack[-1]):
                if self.absValue(collision_stack[-1]) < self.absValue(asteroid):
                    collision_stack.pop()
                    continue
                elif self.absValue(collision_stack[-1]) == self.absValue(asteroid):
                    collision_stack.pop()
                break
            else:
                collision_stack.append(asteroid)

        return collision_stack


if __name__ == "__main__":
    asteroids = [10,2,-5]
    output = Solution().asteroidCollision(asteroids)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
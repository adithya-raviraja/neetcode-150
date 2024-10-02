from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        start_index = 0
        for entry in nums:
            index = start_index
            while index < len(nums):
                if index + 1 == len(nums):
                    index += 1
                    continue
                key = f'{str(start_index)},{str(index+1)}'
                key_rev = f'{str(index+1)},{str(start_index)}'
                if hash_map.get(key, None) == None and hash_map.get(key_rev, None) == None:
                    hash_map[key] = nums[start_index] + nums[index+1]
                
                if hash_map.get(key, None) == target or hash_map.get(key_rev, None) == target:
                    return [int(x) for x in key.split(',')]
                index += 1
            start_index += 1

        return []

if __name__ == "__main__":
    input = [3,4,5,6]
    target = 7
    output = Solution().twoSum(input, target)
    print(output)
    print('TIME COMPLEXITY: O(nlogn)')
    print('SPACE COMPLEXITY: O(n)')
from typing import *
from collections import defaultdict

        # if len(nums) == 0:
        #     return []
        # hash_map = defaultdict(int)
        # top_k_list = list()
        # for num in nums:
        #     hash_map[num] += 1
        
        # hash_rev_map = dict()
        # for key, value in hash_map.items():
        #     hash_rev_map[value] = key

        # num_entries_rev = list(hash_map.values())
        # num_entries_rev.sort(reverse=True)
        
        # index = 0
        # while k > 0:
        #     top_k_list.append(hash_rev_map[num_entries_rev[index]])
        #     index += 1
        #     k -= 1
        # return top_k_list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        
        rev_hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        return list(rev_hash_map.keys())[0:k]


if __name__ == "__main__":
    nums = [1,2,2,3,3,3,3,3]
    k = 2

    k_list = Solution().topKFrequent(nums, k)
    print(k_list)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')
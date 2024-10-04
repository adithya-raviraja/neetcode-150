from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_hash_maps = list()
        final_resp = dict()
        for single_str in strs:
            char_hash_map = dict()
            for char in single_str:
                if char_hash_map.get(char, None) == None:
                    char_hash_map[char] = 1
                else:
                    char_hash_map[char] += 1
            
            if char_hash_map not in all_hash_maps:
                all_hash_maps.append(char_hash_map)
                final_resp[all_hash_maps.index(char_hash_map)] = [single_str]
            else:
                final_resp[all_hash_maps.index(char_hash_map)].append(single_str)

        return list(final_resp.values())

if __name__ == "__main__":
    input = ["act","pots","tops","cat","stop","hat"]
    output = Solution().groupAnagrams(input)
    print(output)
    print('TIME COMPLEXITY: O(n*k)')
    print('SPACE COMPLEXITY: O(n)')
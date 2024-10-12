from typing import *

class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity
        self.list_ref = []

    def get(self, key: int) -> int:
        return self.hash_map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        hash_map_len = len(self.hash_map)
        if self.hash_map.get(key, None) is None:
            if hash_map_len < self.capacity:
                self.hash_map[key] = value
                self.list_ref.append(key)
            if hash_map_len == self.capacity:
                key_to_delete = self.list_ref[0]
                self.list_ref.pop(0)
                self.hash_map.pop(key_to_delete)
                self.hash_map[key] = value
        else:
            self.hash_map[key] = value
        return
    
    def print_stats(self):
        print('HASH_MAP: ', self.hash_map)
        print('CAPACITY: ', self.capacity)

if __name__ == "__main__":
    input = ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
    output = []

    lru_cache = None
    index_count = 0
    for entry in input:
        if entry == 'LRUCache':
            capacity_list = input[index_count + 1]
            lru_cache = LRUCache(capacity_list[0])
            output.append(None)
        elif entry == 'put':
            key_value_list = input[index_count + 1]
            output.append(lru_cache.put(key_value_list[0], key_value_list[1]))
        elif entry == 'get':
            key_list = input[index_count + 1]
            output.append(lru_cache.get(key_list[0]))
        else:
            pass

        index_count += 1
    
    print('INPUT: ', input)
    print('OUTPUT: ', output)

    print('TIME COMPLEXITY: O(1)')
    print('SPACE COMPLEXITY: O(n)')
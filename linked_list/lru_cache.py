from typing import *

class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity
        self.lru_list_head = None
        self.lru_list_tail = None

    def get(self, key: int) -> int:
        hash_data = self.hash_map.get(key, None)
        if hash_data is None:
            return -1
        
        node_entry = hash_data['inst']
        if node_entry.prev:
            node_entry.prev.next = node_entry.next
        else:
            if self.lru_list_head != self.lru_list_tail:
                self.lru_list_head = node_entry.next
        if node_entry.next:
            node_entry.next.prev = node_entry.prev
        node_entry.next = None
        self.lru_list_tail.next = node_entry
        node_entry.prev = self.lru_list_tail
        self.lru_list_tail = node_entry
        return hash_data['data']

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            return
        
        if len(self.hash_map) < self.capacity:
            # self.hash_map[key] = value
            if not self.lru_list_head and not self.lru_list_tail:
                node_entry = ListNode(key)
                self.lru_list_head = self.lru_list_tail = node_entry
                self.hash_map[key] = {
                    'data': value,
                    'inst': node_entry
                }
                return
            else:
                node_entry = ListNode(key)
                self.lru_list_tail.next = node_entry
                node_entry.prev = self.lru_list_tail
                self.lru_list_tail = node_entry
                self.hash_map[key] = {
                    'data': value,
                    'inst': node_entry
                }
                return
        else:
            value_to_pop = self.lru_list_head.val
            self.hash_map.pop(value_to_pop)
            # self.hash_map[key] = value
            if (self.lru_list_head == self.lru_list_tail) and self.capacity == 1:
                self.lru_list_head = self.lru_list_tail = None
            elif (self.lru_list_head == self.lru_list_tail):
                self.lru_list_head = self.lru_list_tail = self.lru_list_head.next
            else:
                self.lru_list_head = self.lru_list_head.next

        node_entry = ListNode(key, next=None, prev=self.lru_list_tail)
        self.lru_list_tail.next = node_entry
        self.lru_list_tail = node_entry

        self.hash_map[key] = {
            'data': value,
            'inst': node_entry
        }
        return
    
    def traverse_list(self):
        head = self.lru_list_head
        front = list()
        while head:
            front.append(head.val)
            head = head.next
        
        tail = self.lru_list_tail
        back = list()
        while tail:
            back.append(tail.val)
            tail = tail.prev

        print('FRONT: ', front)
        print('BACK: ', back)

    def print_stats(self):
        print('HASH_MAP: ', self.hash_map)
        print('CAPACITY: ', self.capacity)

if __name__ == "__main__":
    # input = ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
    # input = ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
    # input = ["LRUCache", [3], "put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], "get", [2], "get", [3], "get", [4], "put", [4, 4], "get", [1], "get", [2], "get", [3], "get", [4]]
    input = ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [1], "get", [2], "get", [3], "get", [1], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
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
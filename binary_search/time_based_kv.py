# Question Link: https://neetcode.io/problems/time-based-key-value-store
from typing import *
import copy

TIMESTAMPS = 'timestamps'
VALUES = 'values'

class TimeMap:
    def __init__(self):
        self.key_store = dict()
        self.values_entry = {
            TIMESTAMPS: list(),
            VALUES: list()
        }
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = copy.deepcopy(self.values_entry)
        
        self.key_store[key][TIMESTAMPS].append(timestamp)
        self.key_store[key][VALUES].append(value)
        return

    def get(self, key: str, timestamp: int) -> str:
        if self.key_store.get(key, "") == "":
            return ""
        
        timestamp_list = self.key_store[key][TIMESTAMPS]
        value_list = self.key_store[key][VALUES]
        low = 0
        high = len(timestamp_list) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if timestamp_list[mid] == timestamp:
                return value_list[mid]
            
            if timestamp > timestamp_list[mid]:
                low = mid + 1
            else:
                high = mid - 1

        if timestamp_list[low - 1] < timestamp:
            return value_list[low - 1]
        else:
            return ""
    

if __name__ == "__main__":
    # input_list = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
    input_list = ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
    output_list = list()

    for index, entry in enumerate(input_list):
        if entry == 'TimeMap':
            timemap_inst = TimeMap()
            output_list.append(None)
        if entry == 'set':
            output_list.append(timemap_inst.set(input_list[index + 1][0], input_list[index + 1][1], input_list[index + 1][2]))
        if entry == 'get':
            output_list.append(timemap_inst.get(input_list[index + 1][0], input_list[index + 1][1]))

    print('INPUT_LIST: ', input_list)
    print('OUTPUT_LIST: ', output_list)

    print('TIME COMPLEXITY SET: O(1)')
    print('TIME COMPLEXITY GET: O(logn)')
    print('SPACE COMPLEXITY: O(m * n)')
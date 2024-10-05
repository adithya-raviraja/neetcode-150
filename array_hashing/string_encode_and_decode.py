import base64
from typing import *

class Solution:
    def __init__(self) -> None:
        self.secret_key = '123Adithya@.com'
        self.replace_blank = '!@#!@!@#!'
        self.replace_space = '!@!!@#!@#!'

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        encoded_str = ''
        count = 0
        for single in strs:
            if count == len(strs) - 1:
                encoded_str += f'{single}'
                continue
            
            count += 1
            encoded_str += f'{single}{self.secret_key}'

        encoded_str = encoded_str.replace('', self.replace_blank)
        encoded_str = encoded_str.replace(' ', self.replace_space)
        encoded_str = base64.b64encode(bytes(encoded_str, 'utf-8')).decode()
        return encoded_str


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return list('')
        
        decoded_str = base64.b64decode(bytes(s, 'utf-8')).decode()
        decoded_str = decoded_str.replace(self.replace_blank, '')
        decoded_str = decoded_str.replace(self.replace_space, ' ')
        split_str = decoded_str.split(self.secret_key)
        res = list()
        for single in split_str:
            res.append(str(single))
        return res

if __name__ == "__main__":
    input = ["hello", "world", "hello"]
    encoded_str = Solution().encode(input)
    print(encoded_str)
    decoded_str = Solution().decode(encoded_str)
    print(decoded_str)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n*k)')
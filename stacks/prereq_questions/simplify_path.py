# Question Link: https://leetcode.com/problems/simplify-path
from typing import *

class Solution(object):
    def simplifyPath(self, path):
        canon_stack = list()
        path_len = len(path)
        i = 0

        while i < path_len:
            if path[i] == '/':
                if canon_stack and canon_stack[-1] != '/' and i + 1 != path_len:
                    canon_stack.append(path[i])
                elif not canon_stack:
                    canon_stack.append(path[i])
                
                i = i + 1
                continue
            elif path[i].isalnum() or path[i] == '_':
                canon_stack.append(path[i])
                i = i + 1
                continue
            elif path[i] == '.':
                dot_count = 0
                while i < path_len and path[i] == '.':
                    dot_count += 1
                    i = i + 1
                
                if dot_count == 1:
                    if (i < path_len and path[i] == '/') or (i >= path_len):
                        if canon_stack[-1] == '/' and len(canon_stack) > 1:
                            canon_stack.pop()
                            continue
                        elif canon_stack[-1] != '/':
                            canon_stack.append('.')
                            continue
                    else:
                        canon_stack.append('.')
                        # i = i + 1
                        continue
                elif dot_count == 2:
                    if (i < path_len and path[i] == '/') or (i >= path_len):
                        if canon_stack[-1] == '/' and len(canon_stack) > 1:
                            canon_stack.pop()
                            while len(canon_stack) > 0 and canon_stack[-1] != '/':
                                canon_stack.pop()
                        elif canon_stack[-1] != '/':
                            canon_stack.append('.')
                            canon_stack.append('.')
                            continue
                    
                    else:
                        canon_stack.append('.')
                        canon_stack.append('.')
                        # i = i + 1
                        continue
                else:
                    j = 0
                    while j < dot_count:
                        canon_stack.append('.')
                        j = j + 1
                    continue
                        
            i = i + 1
      
        if len(canon_stack) > 1 and canon_stack[-1] == '/':
            canon_stack.pop()
        canon_path = ''.join(canon_stack)
        return canon_path


if __name__ == "__main__":
    path = "/hello./world/"
    canon_path = Solution().simplifyPath(path)
    print(canon_path)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')
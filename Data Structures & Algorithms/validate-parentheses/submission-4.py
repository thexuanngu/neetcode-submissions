class Solution:
    def isValid(self, s: str) -> bool:
        matching_close = {')' : '(',
                          '}' : '{',
                          ']' : '['
                          }
        stack = []
        for c in s:
            if c not in matching_close.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if matching_close[c] != stack.pop():
                    return False
        return True if len(stack) == 0 else False
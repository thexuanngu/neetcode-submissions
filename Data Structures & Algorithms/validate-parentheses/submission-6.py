class Solution:
    def isValid(self, s: str) -> bool:
        closers = {")": "(",
                   "}": "{",
                   "]": "["}
        storage = []
        for c in s:
            if c in closers.keys():
                if storage and storage[-1] == closers[c]:
                    storage.pop()
                else:
                    return False
            else:
                storage.append(c)
        return len(storage) == 0
        
        
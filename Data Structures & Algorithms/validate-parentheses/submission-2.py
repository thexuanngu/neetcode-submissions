class Solution:
    def isValid(self, s: str) -> bool:
        closers = {")": "(",
                   "}": "{",
                   "]": "["}
        storage = []
        for char in s:
            if char in closers:
                if storage and storage[-1] == closers[char]:
                    storage.pop()
                else:
                    return False
            else:
                storage.append(char)
        return True if not storage else False
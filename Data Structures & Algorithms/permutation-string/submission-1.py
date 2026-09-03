class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        for start in range(len(s2) - (len(s1) - 1)):
            if (sorted(s1) == sorted(s2[start:start + len(s1)])):
                return True
        return False
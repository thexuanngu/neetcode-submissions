class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        tracker   = []
        for c in s:
            if c not in tracker:
                tracker.append(c)
                maxLength = max(maxLength, len(tracker))
            else:
                while True:
                    if tracker.pop(0) == c:
                        break
                tracker.append(c)
        
        return maxLength if s else 0
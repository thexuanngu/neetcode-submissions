class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base conditions
        if t == "":
            return ""
        if len(t) > len(s):
            return ""

        # Initialize counters
        countT, window = {}, {} # What we need and want to check
        # Just initialize the characters
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        tNeed = len(countT)
        
        # Our results
        res, resLen = [-1, -1], len(s) + 1
        have = 0 # We're going to want to compare how many we have from S to how many we need
        l = 0
        for r in range(len(s)): # Expand the window
            # If s[r] not in countT, we can skip
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == tNeed:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != len(s) + 1 else ""
            
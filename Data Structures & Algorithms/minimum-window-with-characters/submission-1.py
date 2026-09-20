class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base conditions
        if len(t) > len(s) or len(t) == 0:
            return ""

        # Initialize counters
        countT, window = Counter(t), {} # What we need and want to check
        # Compare what we have with what we need:
        tNeed, have = len(countT), 0

        l = 0 # initialize the window
        res, resLen = [-1, -1], len(s) + 1 # initialize the result

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == tNeed:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = l , r
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != len(s) + 1 else ""

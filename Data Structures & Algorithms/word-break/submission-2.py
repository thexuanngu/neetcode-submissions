class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s) + 1) 
        res[-1] = True
        for i in range(len(s) - 1, -1 ,-1):
            for w in wordDict:
                if ((i + len(w) <= len(s)) and (s[i : i + len(w)] == w)):
                    res[i] = res[i + len(w)]
                    if res[0]: # Dealt with the stupid abcd case -> algorithm was working, but at the last step, another match was found which made res[0] false
                        return True
        return res[0]
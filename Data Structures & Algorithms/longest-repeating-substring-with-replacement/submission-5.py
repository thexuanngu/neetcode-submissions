class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        charMap = {}
        maxf = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxf = max(maxf, charMap[s[r]])
            while ((r - l + 1) - maxf) > k:
                charMap[s[l]] = charMap.get(s[l], 0) - 1
                l += 1
            res = max(res, r - l + 1)
        return res
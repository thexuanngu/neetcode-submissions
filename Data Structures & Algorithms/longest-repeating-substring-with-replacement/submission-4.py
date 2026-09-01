class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        charMap = {}
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            while ((r - l + 1) - max(charMap.values())) > k:
                charMap[s[l]] = charMap.get(s[l], 0) - 1
                l += 1
            res = max(res, r - l + 1)
        return res
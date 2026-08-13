class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for offset in range(2):
                l, r = i, i + offset
                while (l >= 0 and r < len(s)):
                    if s[l] != s[r]:
                        break
                    else:
                        l -= 1
                        r += 1
                if len(res) < len(s[l+1:r]):
                    res = s[l+1:r]
        return res
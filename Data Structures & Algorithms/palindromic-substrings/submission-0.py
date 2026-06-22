class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(1, len(s)):
            for j in range(len(s)-i):
                substring = s[j:j+i+1]
                reverse = substring[::-1]
                if substring == reverse:
                    count += 1
        return count
        
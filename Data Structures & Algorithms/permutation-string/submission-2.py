class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        targetString = [0] * 26
        comparisonString = [0] * 26

        for c in s1:
            targetString[ord(c) - ord('a')] += 1

        l, r = 0, 0

        while (r < len(s2)):
            comparisonString[ord(s2[r]) - ord('a')] += 1
            if targetString == comparisonString:
                return True
            r += 1
            if (r - l + 1 > len(s1)):
                comparisonString[ord(s2[l]) - ord('a')] -= 1
                l += 1

        # for start in range(len(s2) - (len(s1) - 1)):
        #     if (sorted(s1) == sorted(s2[start:start + len(s1)])):
        #         return True
        return False
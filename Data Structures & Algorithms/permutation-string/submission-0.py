class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Use a fixed window size!
        charS1Counter = [0] * 26
        charS2Counter = [0] * 26
        for i in range(len(s1)):
            charS1Counter[ord(s1[i]) - ord("a")] += 1
            charS2Counter[ord(s2[i]) - ord("a")] += 1
        matches = 0
        for i in range(26):
            if charS1Counter[i] == charS2Counter[i]:
                matches += 1
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            charS2Counter[index] += 1
            if charS2Counter[index] == charS1Counter[index]:
                matches += 1
            elif charS2Counter[index] == charS1Counter[index] + 1:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            charS2Counter[index] -= 1
            if charS2Counter[index] == charS1Counter[index]:
                matches += 1
            elif charS2Counter[index] == charS1Counter[index] - 1:
                matches -= 1

            l += 1

        return matches == 26
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpTable = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # rows -> text1; cols -> text2

        for i in range(len(text1) - 1, -1 ,-1):
            for j in range(len(text2) - 1, -1 ,-1):
                if text1[i] == text2[j]:
                    dpTable[i][j] = 1 + dpTable[i+1][j+1]
                else:
                    dpTable[i][j] = max(dpTable[i][j+1], dpTable[i+1][j])
        return dpTable[0][0]
                    

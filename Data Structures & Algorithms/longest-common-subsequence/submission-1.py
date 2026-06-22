class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s = len(text1)
        t = len(text2)
        dp = [[0 for _ in range(t + 1)] for _ in range(s + 1)]
        print(dp)
        i, j = 0, 0

        print(dp[i][j])
        maxLen = 0

        for i in range(s - 1, -1, -1):
            for j in range(t - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
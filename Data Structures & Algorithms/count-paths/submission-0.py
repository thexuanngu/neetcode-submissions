class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[[0] for _ in range(n)] for _ in range(m)]
        print(dp[0][0])
        for i in range(m):
            for j in range(n):
                print(dp[i][j])
                print(i,j)
                if i == 0:
                    dp[i][j] = 1
                    continue
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

        
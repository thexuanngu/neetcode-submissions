class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        for i in range(len(coins) - 1, -1, -1):
            print(f"coin: {coins[i]}")
            for j in range(len(dp) - 1, -1, -1):
                if j == len(dp) - 1:
                    dp[j] = 1
                if j + coins[i] < len(dp):
                    dp[j] += dp[j + coins[i]]
            print(f"DP: {dp}")
        return dp[0]

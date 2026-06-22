class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS that ends at i
        for i in range(n): # The shifting window on the right
            for j in range(i): # Consider all combinations 
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

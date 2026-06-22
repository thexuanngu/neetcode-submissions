class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy() # We make a copy so that we can append our result if we don't find it and then reset the DP
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
            dp = nextDP
        return False

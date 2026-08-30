class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, global_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            global_max = max(curSum, global_max)
        return global_max
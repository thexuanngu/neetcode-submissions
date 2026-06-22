class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] # guaranteed one element
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j+1]))
        return max_sum
        
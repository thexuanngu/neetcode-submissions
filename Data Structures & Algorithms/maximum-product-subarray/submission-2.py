class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = minProduct = maxProduct = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            print(nums[i])
            temp1 = min(nums[i], nums[i] * minProduct, nums[i] * maxProduct)
            maxProduct = max(nums[i], nums[i] * minProduct, nums[i] * maxProduct)
            minProduct = temp1
            globalMax = max(globalMax, maxProduct)
        return globalMax
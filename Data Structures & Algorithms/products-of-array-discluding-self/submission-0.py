class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np
        result = []
        for i in range(len(nums)):
            temp = nums.pop(0)
            result.append(np.cumprod(nums)[-1])
            nums.append(temp)
        return result
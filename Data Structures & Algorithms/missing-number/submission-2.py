class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, num in zip(range(1, len(nums) + 1), nums):
            result = result ^ i ^ num
        return result

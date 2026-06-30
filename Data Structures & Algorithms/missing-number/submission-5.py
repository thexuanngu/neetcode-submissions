class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) + 1):
            result ^= i
        nums_XOR = nums[0]
        for i in range(1, len(nums)):
            nums_XOR ^= nums[i]
        return result ^ nums_XOR

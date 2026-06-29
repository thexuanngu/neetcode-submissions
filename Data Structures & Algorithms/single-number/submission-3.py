class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            print(result)
            print(result ^ nums[i])
            result ^= nums[i]

        return result
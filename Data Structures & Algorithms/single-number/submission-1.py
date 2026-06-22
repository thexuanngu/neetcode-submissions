class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = nums.pop(0)
            if temp not in nums:
                return temp
            else:
                nums.remove(temp)
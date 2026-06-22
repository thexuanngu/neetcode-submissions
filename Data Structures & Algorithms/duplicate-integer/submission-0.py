class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set(nums)
        if len(vals) == len(nums):
            return False
        return True

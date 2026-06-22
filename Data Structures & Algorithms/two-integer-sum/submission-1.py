class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # difference -> index
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return[hashmap[nums[i]], i]
            else:
                diff = target - nums[i]
                hashmap[diff] = i
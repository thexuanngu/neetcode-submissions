class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        running_max, max_1s = 0, 0
        for num in nums:
            if num == 0:
                max_1s = max(running_max, max_1s)
                running_max = 0
            else:
                running_max += 1
        max_1s = max(running_max, max_1s)
        return max_1s
        
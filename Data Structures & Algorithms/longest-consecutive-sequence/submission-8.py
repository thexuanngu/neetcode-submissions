class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) <= 1): return len(nums)

        setNums = set(nums)
        possibleStarts = []
        for num in nums:
            if (num - 1) not in setNums:
                possibleStarts.append(num)
        lengthCounter = 0
        for start in possibleStarts:
            count = 1
            while (start + 1) in setNums:
                start += 1
                count += 1
            lengthCounter = max(lengthCounter, count)
        return lengthCounter
                
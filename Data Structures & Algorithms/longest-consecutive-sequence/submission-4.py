class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        count = 1
        temp = 1
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                temp += 1
                print("nums[i]: ", nums[i])
                print("temp:", temp)
                print("count: ", count)
            else:
                count = max(count, temp)
                temp = 1
        count = max(count, temp)
        return count

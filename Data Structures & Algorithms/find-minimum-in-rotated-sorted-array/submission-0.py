class Solution:
    def findMin(self, nums: List[int]) -> int:
        # IF SORTED checks <-> nums[l] < nums[r]
        n = len(nums)
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if (nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            mid = l + (r-l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]: # i.e., on the shift -> we want to find the UNSORTED PART OF THE WINDOW
                l = mid + 1
            else:
                r = mid - 1
        return res


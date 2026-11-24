class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # base, choices, constraints, backtrack
        def backtrack(start, path, curSum):
            # base case: we hit the target or our start is beyond the range of nums
            if curSum == target:
                res.append(path[:])
                return 
            if start == len(nums) or curSum >= target:
                return 

            # choice 1: pick start
            if curSum + nums[start] <= target:
                path.append(nums[start])
                backtrack(start, path, curSum + nums[start])
                path.pop()
            # choice 2: skip start and pick the next
            backtrack(start + 1, path, curSum)
            return res
        return backtrack(0, [], 0)

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # choices, base case, constraints, backtrack
        def backtrack(index, path):
            if (index == len(nums)):  # / starting point
                res.append(path[:])
                return

            path.append(nums[index])  # include the point
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1, path)  # don't include the point
            return res
        return backtrack(0, [])
        
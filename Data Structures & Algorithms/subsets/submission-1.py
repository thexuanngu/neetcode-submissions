class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        # choices, base case, constraints, backtrack
        def backtrack(index, path):
            if (index == len(nums)):
                return res.append(path[:])

            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1, path)
            return res
        return backtrack(0, [])
        
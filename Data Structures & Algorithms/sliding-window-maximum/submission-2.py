class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute Force Solution
        q = collections.deque()
        output = []
        l = r = 0
        while r < len(nums):
            # We want to keep our left most value
            # If the value on the RIGHT > values on the left, pop the earlier values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
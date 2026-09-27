class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixes = [0] * n
        suffixes = [0] * n
        leftMax, rightMax = 0, 0
        for i in range(1, n):
            leftMax = max(leftMax, height[i-1])
            rightMax = max(rightMax, height[n - i])
            prefixes[i] = leftMax
            suffixes[n - i - 1] = rightMax

        res = 0
        for i in range(n):
            res += max(0, min(prefixes[i], suffixes[i]) - height[i])
        return res
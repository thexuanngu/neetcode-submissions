class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n):
            if not stack or (stack and heights[i] > stack[-1][1]):
                stack.append((i, heights[i])) # i.e., 0, 7
            else:  # heights[i] <= stack[-1][1]
                while stack and heights[i] < stack[-1][1]:
                    idx, height = stack.pop()
                    maxArea = max(maxArea, (i - idx) * height)
                    if not stack or (heights[i] > stack[-1][-1]):
                        stack.append((idx, heights[i]))
        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, (n-idx)*height)
        return maxArea
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            limiting_wall = (min(heights[l], heights[r]))
            temp_area = (r - l) * limiting_wall
            area = max(area, temp_area)
            if heights[l] == limiting_wall:
                l += 1
            else:
                r -= 1
        return area


class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int areaMax = 0;
        while (l < r) {
            int leftHeight = heights[l], rightHeight = heights[r];
            areaMax = max(areaMax, (r-l) * min(rightHeight, leftHeight));
            if (rightHeight < leftHeight) {
                r--;
            } else {
                l++;
            }
        }
        return areaMax;
    }
};

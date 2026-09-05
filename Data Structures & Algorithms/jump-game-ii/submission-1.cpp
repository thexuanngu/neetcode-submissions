class Solution {
public:
    int jump(vector<int>& nums) {
        int minJumps = 0, farthestReach = 0, currentEnd = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            farthestReach = max(farthestReach, i + nums[i]);
            if (i == currentEnd) {
                minJumps++;
                currentEnd = farthestReach;
            }
        }
        return minJumps;
    }
};
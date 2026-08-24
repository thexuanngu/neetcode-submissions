class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int globalMax = nums[0], curSum = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            curSum = max(nums[i], curSum + nums[i]);
            globalMax = max(globalMax, curSum);
        }
        return globalMax;
    }
};

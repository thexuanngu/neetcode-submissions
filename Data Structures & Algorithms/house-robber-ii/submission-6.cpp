class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums.front();
        int max1 = houseRob(nums, 0, nums.size() - 1);
        int max2 = houseRob(nums, 1, nums.size());
        return max(max1, max2);
    }

    int houseRob(vector<int>& nums, size_t start, size_t end) {
        int prev   = 0;
        int result = 0;
        for (int i = start; i < end; ++i) {
            int temp = result;
            result = max(result, prev + nums[i]);
            prev = temp;
        }
        return result;
    }
};

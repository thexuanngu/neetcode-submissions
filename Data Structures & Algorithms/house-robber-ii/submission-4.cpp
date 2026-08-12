class Solution {
public:
    int robLinear(vector<int>& nums, int lo, int hi) {
    int prev1 = 0, prev2 = 0;
    for (int i = lo; i <= hi; i++) {
        int temp = max(prev1, prev2 + nums[i]);
        prev2 = prev1;
        prev1 = temp;
    }
    return prev1;
}

int rob(vector<int>& nums) {
    if (nums.size() == 1) return nums[0];
    return max(robLinear(nums, 0, nums.size()-2),
               robLinear(nums, 1, nums.size()-1));
}
};

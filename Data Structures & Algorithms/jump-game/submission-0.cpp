class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.empty()) return false;
        int closestJumpIndex = nums.size() - 1;
        for (int i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] + i >= closestJumpIndex) {
                closestJumpIndex = i;
            }
        }
        return closestJumpIndex == 0;
    }
};

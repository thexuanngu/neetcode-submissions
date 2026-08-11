class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        int tempa1 = 0, max1 = 0, tempb1 = 0, max2 = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            int temp1 = max1;
            int temp2 = max2;
            max1 = max(max1, tempa1 + nums[i]);
            max2 = max(max2, tempb1 + nums[i+1]);
            tempa1=temp1;
            tempb1=temp2;
        }
        return max(max1, max2);
    }
};

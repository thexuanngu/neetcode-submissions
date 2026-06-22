class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> numSet{};
        for (int i{}; i < nums.size(); ++i) {
            numSet.insert(nums.at(i));
            if (i + 1 != numSet.size()) {
                return true;
            }
        }
        return false;
    }
};
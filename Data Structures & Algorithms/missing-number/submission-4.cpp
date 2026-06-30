class Solution {
public:
    int missingNumber(vector<int>& nums) {
        set<int> hashSet = {};
        for (int num : nums) hashSet.insert(num);
        for (int i = 0; i < nums.size() + 1; ++i) {
            if (hashSet.contains(i) == false) return i;
        }
}
};

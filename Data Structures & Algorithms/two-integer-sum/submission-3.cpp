class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap = {};

        for (int i{}; i < nums.size(); ++i) {
            if (hashmap.find(target - nums[i]) != hashmap.end()) return vector<int> {hashmap[target - nums[i]], i};
        hashmap.insert(make_pair(nums[i], i));
        }
    }
};

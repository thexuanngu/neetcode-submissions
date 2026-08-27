class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);
        // map -> ordered keys (slower insert because of comparison)
        unordered_map<int, int> hashMap;
        for (const auto& num : nums) {
            hashMap[num]++;
        }
        for (const auto& pair : hashMap) {
            buckets[pair.second].push_back(pair.first);
        }
        int counter = 0;
        vector<int> result;
        for (size_t i = buckets.size() - 1; i >= 0; --i) {
            if (buckets[i].empty()) continue;
            for (int element : buckets[i]) {
                result.push_back(element);
                counter++;
                if (counter == k) return result;
            }
        }
    }
};

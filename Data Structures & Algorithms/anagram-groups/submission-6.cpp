class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> hashMap;
        for (auto s : strs) {
            vector<int> encode(26);
            for (auto c : s) {
                encode[int(c) - int('a')]++;
            }
            hashMap[encode].push_back(s);
        }
        vector<vector<string>> result;
        for (auto pair : hashMap) {
            result.push_back(pair.second);
        }
        return result;
    }
};

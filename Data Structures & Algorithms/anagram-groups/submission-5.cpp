class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> hashmap;
        for (auto s : strs) {
            vector<int> letter_count(26, 0);
            for (char c : s) {
                letter_count[int(c) - int('a')]++;
            }
            hashmap[letter_count].push_back(s);
        }
        vector<vector<string>> result;
        for (auto it = hashmap.begin(); it != hashmap.end(); it++) {
            result.push_back(it->second);
        }
        return result;
    }
};

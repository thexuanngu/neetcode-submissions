class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> index_map;
        int i = 0, maxLength = 0;

        for (int j = 0; j < s.size(); j++) {
            if (index_map.count(s[j])) {
                i = max(i, index_map[s[j]] + 1);
            }
            index_map[s[j]] = j;
            maxLength = max(maxLength, j - i + 1);
        }
        return maxLength;
    }
};
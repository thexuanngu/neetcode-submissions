class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) return 0;
        unordered_map<char, int> index_map = {{s[0], 0}};
        int i = 0, j = 1, maxLength = 1;

        while (j < s.size()) {
            if (index_map.count(s[j]) == 0) {
                index_map[s[j]] = j;
                j++;
            } else {
                maxLength = max(maxLength, j - i);
                i = max(i, index_map[s[j]] + 1);
                index_map[s[j]] = j;
                j++;
            }
        }
        maxLength = max(maxLength, j - i);
        return maxLength;
    }
};

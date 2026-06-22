class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> wordCount(26, 0);

        for (int i{}; i < s.size(); ++i) {
            wordCount[int(s[i]) - int('a')] += 1;
            wordCount[int(t[i]) - int('a')] -= 1;
        }

        for (int letter : wordCount) {
            if (letter != 0) return false;
        }
        return true;
    }
};

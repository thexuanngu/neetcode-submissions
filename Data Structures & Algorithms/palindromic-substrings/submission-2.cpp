class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.size(); ++i) {
            for (int offset = 0; offset < 2; ++offset) {
                int l = i, r = i + offset;
                while (l >= 0 && r < s.size()) {
                    if (s[l] != s[r]) {
                        break;
                    } else {
                        count++;
                        l--;
                        r++;
                    }
                }
            }
        }
        return count;
    }
};

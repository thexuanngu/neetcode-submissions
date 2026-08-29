class Solution {
public:
    string longestPalindrome(string s) {
        string result = "";
        for (int i = 0; i < s.size(); i++) {
            for (int offset = 0; offset < 2; offset++) {
                int l = i, r = i + offset;
                while (l >=0  && r < s.size()) {
                    if (s[l] != s[r]) {
                        break;
                    }
                    l--;
                    r++;
                }
                string temp(s.begin() + l + 1, s.begin() + r);
                if (result.size() < temp.size()) {
                    result = temp;
                }
            }
        }
        return result;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        string result = "";
        for (int i = 0; i < (int)s.size(); i++) {
            for (int offset = 0; offset < 2; offset++) {
                int l = i, r = i + offset;
                while (l >= 0 && r < (int)s.size() && s[l] == s[r]) {
                    l--;
                    r++;
                }
                // palindrome is now s[l+1 .. r-1]
                string temp = s.substr(l + 1, r - l - 1);
                if (result.size() < temp.size()) {
                    result = temp;
                }
            }
        }
        return result;
    }
};
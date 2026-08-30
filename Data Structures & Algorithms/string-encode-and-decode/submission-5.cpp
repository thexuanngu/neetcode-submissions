class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (string& s : strs) {
            result += std::format("{}~{}", s.size(), s);
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result = {};
        if (s == "") {
            return result;   
        }
        
        int i = 0;
        while (i < s.size()) {
            int j = i + 1;
            while (s[j] != '~') {
                j++;
            }
            int length = stoi(s.substr(i, j-i));
            i = j + 1;
            result.push_back(s.substr(i, length));
            i += length;
        }
        return result;
    }
};

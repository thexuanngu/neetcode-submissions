class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> counter_s;
        std::unordered_map<char, int> counter_t;

        for (int i = 0; i < s.size(); i++) {
            counter_s[s[i]]++;
            counter_t[t[i]]++;
        }

        return (counter_s == counter_t);

    }
};

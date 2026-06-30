class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> result(n + 1, 0);
        for (int i = 1; i < n + 1; ++i) {
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
        
    }
};

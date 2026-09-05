class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        if (text1.size() < text2.size()) {
            swap(text1, text2);
        }
        std::vector<int> currArray(text2.size() + 1, 0);
        std::vector<int> prevArray(text2.size() + 1, 0);

        for (int i = text1.size() - 1; i >= 0; --i) {
            for (int j = text2.size() - 1; j >= 0; --j) {
                if (text1[i] == text2[j]) {
                    currArray[j] = 1 + prevArray[j + 1];
                } else {
                    currArray[j] = max(currArray[j + 1], prevArray[j]);
                }
            }
            prevArray = currArray;
        }
        return currArray[0];
    }
};
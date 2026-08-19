class Solution {
public:
    bool isValid(string s) {
        std::stack<char> charStack;
        std::unordered_map<char, char> closeToOpen = {
            {'}' , '{'},
            {']' , '['},
            {')' , '('}
        };

        for (char c : s) {
            if (closeToOpen.count(c)) {
                if (!charStack.empty() && closeToOpen[c] == charStack.top()) {
                    charStack.pop();
                } else {
                    return false;
                }
            } else {
                charStack.push(c);
            }
        }
        return charStack.empty();
    }
};

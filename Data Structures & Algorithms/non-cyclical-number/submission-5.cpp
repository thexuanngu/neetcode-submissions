class Solution {
public:
    bool isHappy(int n) {
        auto slow = n, fast = n;
        while (fast != 1) {
            slow = sumOfSquares(slow);
            fast = sumOfSquares(fast);
            fast = sumOfSquares(fast);
            if (fast == slow && fast != 1) {
                return false;
            }
        }
        return true;
    }

    int sumOfSquares(int n) {
        auto result = 0;
        while (n) {
            auto digit = n % 10;
            result += digit * digit;
            n /= 10;
        }
        return result;
    }
};

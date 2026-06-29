class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = sumOfSquares(n);
        while (slow != fast) {
            fast = sumOfSquares(fast);
            fast = sumOfSquares(fast);
            slow = sumOfSquares(slow);
        }
        return fast == 1;
    }

    int sumOfSquares(int n) {
        int output = 0;
        while (n) {
            int digit = n % 10;
            output += digit * digit;
            n /= 10;
        }
        return output;
    } 
};

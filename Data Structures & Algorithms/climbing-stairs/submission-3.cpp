class Solution {
public:
    int climbStairs(int n) {
        int temp1 = 1, temp2 = 1;
        for (int i = 1; i < n; i++) {
            int temp = temp2;
            temp2 += temp1;
            temp1 = temp;
        }
        return temp2;
    }
};

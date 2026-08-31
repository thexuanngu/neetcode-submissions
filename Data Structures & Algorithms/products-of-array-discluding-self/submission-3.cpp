class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);

        // result[i] holds prefix product of everything before i
        for (int i = 1; i < n; i++) {
            result[i] = result[i-1] * nums[i-1];
        }

        // fold in suffix product using a running variable instead of an array
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }

        return result;
    }
};
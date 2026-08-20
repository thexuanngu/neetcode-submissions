class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int length = r - l;
            int mid = l + ((length) / 2);
            // std::cout << "mid: " << mid << std::endl;
            // std::cout << "l: " << l << std::endl;
            if (nums[mid] == target) {
            // std::cout << "target == true " << l << std::endl;
                return mid;
            } else if (nums[mid] > target) {
            // std::cout << "target is smaller " << l << std::endl;
                r = mid - 1;
                
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }
};

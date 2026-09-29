class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        // Goal: find the rotation point
        while (l < r) {
            int mid = l + (r-l) / 2;
            // std::cout<<mid<<nums[mid]<<std::endl;
            if (nums[l] < nums[r]) {
                break;
            }
            else if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        std::cout<<l<<std::endl;
        // l = pivot index = start of sequence
        // I need to find which side the minimum of the array could be optional
        r = nums.size() - 1;
        if (nums[l] < target) {
            if (target > nums[r]) {
                r = l - 1;
                l = 0;
            }
        } else {
            return (nums[l] == target) ? l : -1;
        }
            std::cout << l << std::endl;

        while (l <= r) {
            int mid = l + ((r-l) / 2);
            std::cout << mid << std::endl;
            
            std::cout << "BOI" << nums[mid] << std::endl;
            
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] > target) {
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
            std::cout << nums[l] << std::endl;

        return (nums[l] == target) ? l : -1;
    }
};

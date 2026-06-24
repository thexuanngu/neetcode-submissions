class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0, l = 0, r = 1;
        if (prices.size() == 1) return 0;
        while (r < prices.size()) {
            if (prices[l] < prices[r]) max_profit = max(max_profit, prices[r] - prices[l]);
            else l = r;
            r++;
        }
        return max_profit;
    }
};

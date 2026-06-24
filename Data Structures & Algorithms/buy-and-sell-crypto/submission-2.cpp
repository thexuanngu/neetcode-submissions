class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        if (prices.size() == 1) return 0;

        for (int l = 0; l < prices.size() - 1; l++) {
            for (int r = l + 1; r < prices.size(); r++) {
                if (prices[r] - prices[l] > max_profit) max_profit = prices[r] - prices[l];
            }
        }

        return max_profit;
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int min_buy = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            max_profit = max(max_profit, prices[i] - min_buy);
            min_buy = min(prices[i], min_buy);
        }
        return max_profit;
    }
};

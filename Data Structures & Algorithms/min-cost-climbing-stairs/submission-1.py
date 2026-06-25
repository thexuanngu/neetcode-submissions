class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCosts = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                minCosts[i] = cost[i]
            else:
                minCosts[i] = cost[i] + min(minCosts[i + 1], minCosts[i + 2])
        return min(minCosts[0], minCosts[1])
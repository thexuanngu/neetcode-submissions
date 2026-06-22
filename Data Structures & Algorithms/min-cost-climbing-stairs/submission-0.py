class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        s1 = cost[0]
        s2 = cost[1]
        for i in range(2, len(cost)):
            temp = s2
            s2 = cost[i] + min(s1, s2)
            s1 = temp
        return s2
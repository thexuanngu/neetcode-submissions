class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            if i + 1 == n:
                steps[i] = 1
            elif i + 2 == n:
                steps[i] = 2
            else:
                steps[i] = steps[i+1] + steps[i+2]
        return steps[0]
class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1, 1
        for i in range(1, n):
            temp = s2
            s2 += s1
            s1 = temp
        return s2

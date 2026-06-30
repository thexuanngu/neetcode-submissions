class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(self.count1s(i))
        return result

    def count1s(self, n: int) -> int:
        res = 0
        while (n):
            n &= n-1
            res += 1
        return res
            

class Solution:
    def hammonAlgo(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        for i in range(n+1):
            output[i] = self.hammonAlgo(i)
        return output

    
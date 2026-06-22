class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            n = [int(i) for i in str(n)]
            return sum([i ** 2 for i in n])
        
        
        result = helper(n)
        hashset = set()
        hashset.add(result)
        while result != 1:
            result = helper(result)
            if (result in hashset) and (result != 1):
                return False
            hashset.add(result)

        return True
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            n = [int(i) for i in str(n)]
            return sum([i ** 2 for i in n])

        def helper2(n):
            output = 0

            while n:
                digit = n % 10
                digit *= digit
                output += digit
                n = n // 10
            return output

        
        result = helper(n)
        hashset = set()
        hashset.add(result)
        while result != 1:
            result = helper2(result)
            if (result in hashset) and (result != 1):
                return False
            hashset.add(result)

        return True
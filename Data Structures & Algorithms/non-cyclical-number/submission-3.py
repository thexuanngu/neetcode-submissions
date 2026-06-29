class Solution:
    def isHappy(self, n: int) -> bool:
        numbersSeen = [n]
        while (True):
            if n == 1:
                return True
            temp = 0
            digits = len(str(n))
            for _ in range(digits):
                digit = n % 10
                temp += digit ** 2
                n = n // 10
            if temp in numbersSeen:
                return False
            numbersSeen.append(temp)
            n = temp
            
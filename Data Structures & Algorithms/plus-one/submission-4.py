class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i != 0:
                i -= 1
            else:
                digits.insert(0, 1)
                return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for d in digits:
            number += number.join(str(d))
        number = str(int(number) + 1)
        return [int(d) for d in str(number)]
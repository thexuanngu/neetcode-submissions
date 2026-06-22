class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            r = i + 1
            temp = target - numbers[i]
            while r < len(numbers):
                if numbers[r] == temp:
                    return [i + 1, r + 1]
                r += 1
            
        
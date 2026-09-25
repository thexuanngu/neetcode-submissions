class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0: # If divisible by 2, you can keep smash all of them
                first -= 1 # Go to the next lowest weight
                continue
            
            j = min(first - 1, second) # Find the second weight to smash
            while j > 0 and bucket[j] == 0: # If there are no stones of that weight, move on
                j -= 1
            
            if j == 0: # If you end up at 0 -> the second stone is 0 -> therefore only the first weight
                return first
            second = j
            bucket[first] -= 1 # lose a stone here
            bucket[second] -= 1 # lose a stone here
            bucket[first-second] += 1 # add the new stone here
            first = max(first-second, second) # because there would be even stones left possibly, so cannot be any big ones left

        return first
            


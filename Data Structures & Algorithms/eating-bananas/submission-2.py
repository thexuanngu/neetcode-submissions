from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r  = 1, max(piles)
        minK = 0
        while l <= r:
            mid = l + (r-l) // 2
            if sum(ceil(x/mid) for x in piles) > h:
                l = mid + 1
            else:
                minK = mid
                r = mid-1
        return minK



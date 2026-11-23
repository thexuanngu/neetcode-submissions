class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return the k closest points -> if we can organize points into a heap, we can just grab the k closest
        # to turn into a heap, we need to compute their distance
        # we could also use a sorting function?

        # guaranteed to have at least 1 point
        points.sort(key=lambda x: math.sqrt((x[0] ** 2) + (x[1] ** 2)))
        return points[:k]
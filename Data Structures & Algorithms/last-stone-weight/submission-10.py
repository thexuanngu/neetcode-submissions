class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)
            new_s = s1 - s2
            if new_s != 0:
                heapq.heappush(maxHeap, -new_s)
        return -maxHeap[0] if len(maxHeap) > 0 else 0
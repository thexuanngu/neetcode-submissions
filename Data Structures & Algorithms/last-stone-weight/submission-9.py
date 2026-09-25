class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            heavyBoi = heapq.heappop(maxHeap)
            heavyBoi2 = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, heavyBoi-heavyBoi2)
        return 0 if len(maxHeap) == 0 else -maxHeap[0]
        
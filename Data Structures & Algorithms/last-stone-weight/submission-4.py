class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-stone for stone in stones]
        heapq.heapify(stoneHeap)
        while (len(stoneHeap) > 1):
            first = heapq.heappop(stoneHeap)
            second = heapq.heappop(stoneHeap)
            if (first != second):
                heapq.heappush(stoneHeap, first-second)
        return -stoneHeap[0] if stoneHeap else 0


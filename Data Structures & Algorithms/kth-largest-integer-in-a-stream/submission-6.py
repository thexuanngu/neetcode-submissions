class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = [num for num in nums]
        heapq.heapify(self.maxHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        var = heapq.nlargest(self.k, self.maxHeap)
        return var[-1]
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucketSort = [[] for _ in range(len(nums))]
        for num, count in counter.items():
            bucketSort[count-1].append(num)
        res = []
        tracker = 0
        for i in range(len(bucketSort)-1, -1, -1):
            if not bucketSort[i]:
                continue;
            for item in bucketSort[i]:
                res.append(item)
                tracker+=1
                if tracker == k:
                    break
            if tracker == k:
                break
        return res
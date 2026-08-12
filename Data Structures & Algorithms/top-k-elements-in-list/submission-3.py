class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucketSort = [[] for _ in range(len(nums) + 1)]  # see note below
        for num, count in counter.items():
            bucketSort[count].append(num)  # count itself, no -1 needed
        res = []
        for i in range(len(bucketSort) - 1, 0, -1):
            for item in bucketSort[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return res
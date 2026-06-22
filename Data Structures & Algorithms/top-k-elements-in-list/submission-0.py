class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Initial Solution:
        1. Get the count of each unique element in nums
        2. 
        '''
        # Get the count
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        sorted_nums = sorted(counter.items(), key = lambda item: -item[1])

        result = []
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result
        


        
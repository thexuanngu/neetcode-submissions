class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Initial Solution (naive):
        1. Get the count of each unique element in nums
        2. Sort the nums by their values
        3. Return the k-most frequent
        '''
        # Get the count
        # counter = {}
        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        # sorted_nums = sorted(counter.items(), key = lambda item: -item[1])

        # result = []
        # for i in range(k):
        #     result.append(sorted_nums[i][0])
        # return result

        '''
        Method 2: Bucket Sort Algorithm
        Key idea: Create buckets from 1 - n
        '''
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
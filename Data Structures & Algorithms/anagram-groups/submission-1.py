class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap Solution
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)

        return list(hashmap.values())

        # Sorted solution.
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
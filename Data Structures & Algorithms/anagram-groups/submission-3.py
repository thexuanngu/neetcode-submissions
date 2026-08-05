class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for s in strs:
            letter_count = [0 for _ in range(26)]
            for c in s:
                letter_count[ord(c) - ord('a')] += 1
            storage[tuple(letter_count)].append(s)
        res = []
        for v in storage.values():
            res.append(v)
        return res if storage.values() else [[""]]
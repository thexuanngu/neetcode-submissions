class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + "#" + s
        return result



        # if not strs:
        #     return []
        # result = ''
        # for s in strs:
        #     result = result + s
        #     if s != strs[-1]:
        #         result = result + '&'
        # return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for ops in operations:
            if ops == "C":
                results.pop()
            elif ops == "D":
                results.append(2 * results[-1])
            elif ops == "+":
                results.append(results[-1] + results[-2])
            else:
                results.append(int(ops))
        return sum(results)
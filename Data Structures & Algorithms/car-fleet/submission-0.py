class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # positions are unique:
        positionMap = {}
        for i, p in enumerate(position):
            positionMap[p] = i
        sortedPositions = sorted(position)

        fleets = 0
        while sortedPositions:
            p = sortedPositions.pop()
            v = speed[positionMap[p]]
            t = (target - p) / v
            while sortedPositions and t >= (target - sortedPositions[-1]) / speed[positionMap[sortedPositions[-1]]]:
                sortedPositions.pop()
            fleets += 1

        return fleets
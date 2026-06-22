class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            bigg_stone = stones.pop(0)
            big_stone = stones.pop(0)
            new_stone = bigg_stone - big_stone
            if new_stone <= 0:
                continue
            else:
                stones.append(new_stone)
            print(stones)

        return stones[0] if stones else 0


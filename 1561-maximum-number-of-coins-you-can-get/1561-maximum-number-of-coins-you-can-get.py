class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_coins = 0
        sorted_piles = sorted(piles, reverse=True)
        for i in range(1, (int((len(piles) / 3 )*2)), 2):
            my_coins += sorted_piles[i]

        return my_coins
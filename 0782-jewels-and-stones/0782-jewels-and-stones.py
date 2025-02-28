class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    output += 1
        return output

            
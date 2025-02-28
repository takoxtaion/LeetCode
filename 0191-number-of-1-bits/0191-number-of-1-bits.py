class Solution:
    def hammingWeight(self, n: int) -> int:
        new_list = [i for i in bin(n)][2:]
        return new_list.count("1")
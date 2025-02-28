class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
            count += 1
        return n == 1
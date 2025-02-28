class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        a = str(x)[::-1]
        if n == a:
            return True
        else:
            return False
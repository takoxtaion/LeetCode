class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = sorted(s)
        n = sorted(t)
        if m == n:
            return True
        else:
            return False
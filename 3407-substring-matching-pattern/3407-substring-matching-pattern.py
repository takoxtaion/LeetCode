class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        parts = p.split('*')
        pfx = parts[0]
        sfx = parts[1]
        first = s.find(pfx)
        if first == -1:
            return False
        return sfx in s[first + len(pfx):]
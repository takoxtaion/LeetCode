class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ''
        anbani = 'abcdefghijklmnopqrstuvwxyz0123456789'            
        for i in s1:
            if i in anbani:
                s2 += i
        return s2[::-1] == s2
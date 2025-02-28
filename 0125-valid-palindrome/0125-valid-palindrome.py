class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ''
        anbani = 'abcdefghijklmnopqrstuvwxyz0123456789'            
        for i in s1:
            if i in anbani:
                s2 += i
        s3 = s2[::-1]
        if s3 == s2:
            return True
        else:
            return False
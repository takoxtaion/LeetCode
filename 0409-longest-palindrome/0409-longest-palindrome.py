class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        longest_palindrome = 0
        odd = False
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for count in count.values():
            longest_palindrome += count // 2 * 2
            if count % 2 == 1:
                odd = True
        if odd:
            longest_palindrome += 1

        return longest_palindrome
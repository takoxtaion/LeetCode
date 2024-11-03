def isPalindrome(x):
    result = True if str(x) == str(x)[::-1] else False
    return result
#Example      
print(isPalindrome(121))

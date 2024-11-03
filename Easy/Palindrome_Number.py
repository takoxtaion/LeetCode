def isPalindrome(x):
    result = True if str(x) == str(x)[::-1] else False
    return result
      
print(isPalindrome(121))

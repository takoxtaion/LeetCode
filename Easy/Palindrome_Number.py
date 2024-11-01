def isPalindrome(x):
    n = str(x)
    a = str(x)[::-1]
    if n == a:
        return True
    else:
        return False
      
print(isPalindrome(121))

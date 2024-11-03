def isAnagram(s, t) -> bool:
    result = True if sorted(s) == sorted(t) else False:
    return result
#Example
print(isAnagram("anagram", "nagaram"))

def isAnagram(s, t) -> bool:
    result = True if sorted(s) == sorted(t) else False:
    return result

print(isAnagram("anagram", "nagaram"))

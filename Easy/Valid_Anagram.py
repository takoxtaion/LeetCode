def isAnagram(s, t) -> bool:
    m = sorted(s)
    n = sorted(t)
    if m == n:
        return True
    else:
        return False

print(isAnagram("anagram", "nagaram"))

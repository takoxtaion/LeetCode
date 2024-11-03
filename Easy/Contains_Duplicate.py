def containsDuplicate(nums) -> bool:
    result = True if len(nums) != len(set(nums)) else False
    return result


print(containsDuplicate([1, 2, 3, 1]))

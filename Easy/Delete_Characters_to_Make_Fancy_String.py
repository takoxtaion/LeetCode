def makeFancyString(s):
    result = []
    count = 0
    for i in s:
        if result and result[-1] == i:
            count += 1
        else:
            count = 1
        if count <= 2:
            result.append(i)
    return "".join(result)


# Example:
print(makeFancyString("LeeetCode"))

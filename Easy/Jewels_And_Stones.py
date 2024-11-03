def numJewelsInStones(jewels, stones):
    output = 0
    for i in jewels:
        for j in stones:
            if i == j:
                output += 1
    return output
#example
print(numJewelsInStones("aA", "aAAbbbb"))

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0
        for char in s:
            if result and result[-1] == char:
                count += 1
            else:
                count = 1  
            if count <= 2: 
                result.append(char)
        return "".join(result)
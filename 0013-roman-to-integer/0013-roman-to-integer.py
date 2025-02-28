class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        my_dict = {
        "I" : 1,
        "IV": 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
        }

        curr = 0
        for i in range(len(s)): 
            if curr < len(s) - 1 and s[curr:curr + 2] in my_dict:  
                num += my_dict[s[curr:curr + 2]]
                curr += 2  
            elif curr < len(s):  
                num += my_dict[s[curr]]
                curr += 1

        return num
class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        list = [i for i in command]

        for i in range(1, len(list)):
            if list[i-1] == "(" and list[i] == ")":
                list[i-1] = ""
                list[i] = "o"
            if list[i-1] == "(" and list[i] != ")":
                list[i-1] = ""            
            if list[i] == ")" and list[i-1] != "(":
                list[i] = ""    

        for i in list:
            result += i   
        return result
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1, num_2 = 0, 0
        my_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
    }
        
        my_dict_1 = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
    }
        for i in range(len(num1)): 
            num_1 += my_dict.get(num1[i]) * (10 ** ((i-(len(num1))) * (-1) - 1))
        for i in range(len(num2)):
            num_2 += my_dict.get(num2[i]) * (10 ** ((i-(len(num2))) * (-1) - 1))

        product = num_1 * num_2
        product_copy = product


        list_of_product_dgs = []


        len_product = 1
        while product_copy >= 10:  
            product_copy //= 10
            len_product += 1

        for i in range(len_product, 0, -1):
            n = product // 10 ** (i - 1)
            product -= n * (10 ** (i - 1))
            list_of_product_dgs.append(n)

        output = ""

        for i in list_of_product_dgs:
            output += my_dict_1[i]

        return output